#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compile wiki_data.json segments into the daily-briefing chain universe.

Usage:
    python3 L3-网页产物/build_chain_universe.py
    python3 L3-网页产物/build_chain_universe.py INPUT OUTPUT
"""

import datetime
import hashlib
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = SCRIPT_DIR / "wiki_data.json"
DEFAULT_OUTPUT = SCRIPT_DIR / "chain_universe.json"
LOGIC_VERSION = "canonical-segments-v2"

# Exact cross-track duplicate names in AI算力 and 半导体.
CANONICAL_SEGMENT_ALIASES = {
    "光刻机": "lithography",
    "封装基板材料": "package-substrate",
    "电子特气": "electronic-gas",
    "薄膜沉积设备": "thin-film-deposition",
    "Chiplet与异构集成": "chiplet",
    "CPU(服务器级)": "server-cpu",
    "高纯硅料与硅片": "silicon-wafer",
    "检测量测设备": "inspection-metrology",
    "RISC-V AI芯片": "riscv-ai",
    "刻蚀设备": "etch-equipment",
    "光刻胶与湿化学品": "photoresist",
    "高速连接器与铜缆": "high-speed-connector",
    "晶圆代工(先进制程)": "foundry-advanced",
    "EDA与IP核": "eda-ip",
    "溅射靶材": "sputtering-target",
    "FPGA": "fpga",
}

TICKER_ALIASES = {
    "005930": "005930.KS",
    "000660": "000660.KS",
    "2344": "2344.TW",
    "2408": "2408.TW",
    "3037": "3037.TW",
    "3711": "3711.TW",
    "4062": "4062.T",
    "4063": "4063.T",
    "4005": "4005.T",
    "4091": "4091.T",
    "4901": "4901.T",
    "5016": "5016.T",
    "6239": "6239.TW",
    "6488": "6488.TW",
    "6967": "6967.T",
    "8046": "8046.T",
    "9660": "9660.T",
    "0700": "0700.HK",
    "0992": "0992.HK",
    "9988": "9988.HK",
    "9888": "9888.HK",
    "9698": "9698.HK",
    "2454": "2454.TW",
    "2498": "2498.TW",
    "2802": "2802.T",
    "KIOXIA": "285A.T",
    "2308": "2308.TW",
    "2325": "2325.TW",
    "2449": "2449.TW",
    "285A": "285A.T",
    "4042": "4042.T",
    "5201": "5201.T",
    "5384": "5384.T",
    "6302": "6302.T",
    "6361": "6361.T",
    "6503": "6503.T",
    "6728": "6728.T",
    "6824": "6824.T",
    "6971": "6971.T",
    "7735": "7735.T",
    "7912": "7912.T",
    "8299": "8299.TW",
    "ABBN": "ABBN.SW",
    "ATS": "ATS.VI",
    "OVH": "OVH.PA",
    "PFV": "PFV.DE",
    "SMIC": "0981.HK",
    "AI": "AI.PA",
    "SU": "SU.PA",
    "SEMCO": "009150.KS",
}

PRIVATE_TICKERS = {
    "未上市",
    "HUAWEI",
    "HUAWEI-POWER",
    "BYTEDANCE",
    "OPENAI",
    "ANTHROPIC",
    "DEEPSEEK",
    "HUGGINGFACE",
    "MTHREAD",
    "BIREN",
    "ILUVATAR",
    "CXMT",
    "YMTC",
    "KUNLUN",
    "CBRS",
    "GRAPH",
    "SAMBA",
    "MOONSHOT",
    "BAICHUAN",
    "FIGURE",
    "ONEX",
    "COHERE",
    "XAI",
    "MISTRAL",
    "STABILITY",
    "TOGETHER",
    "FIREWORKS",
    "RUNPOD",
    "MODAL",
    "ANYSCALE",
    "SCALE",
    "CRUSOE",
    "DATABRICKS",
    "FUNGIBLE",
    "PERP",
    "GROQ",
    "LAMBDA",
    "NURO",
    "CURSOR",
    "REPLIT",
    "WANDB",
    "JETBRAINS",
    "BOSCH",
    "CD",
    "SP",
    "CYRUS",
    "VANTAGE",
    "EDGECONNEX",
    "STACK",
    "COOLIT",
    "ICEOTOPE",
    "SUBMER",
    "ZUTACORE",
    "RIELLO",
    "CYXT",
    "TSP",
    "ZHIPU",
    "ZOXX",
}

MARKET_BY_SUFFIX = {
    ".KS": "KR",
    ".KQ": "KR",
    ".T": "JP",
    ".TW": "TW",
    ".TWO": "TW",
    ".HK": "HK",
    ".SS": "CN",
    ".SZ": "CN",
    ".DE": "DE",
    ".AS": "NL",
    ".PA": "FR",
    ".L": "GB",
    ".MI": "IT",
    ".SW": "CH",
    ".TO": "CA",
    ".V": "CA",
}


def normalize_ticker(ticker):
    raw = str(ticker or "").strip().upper()
    return TICKER_ALIASES.get(raw, raw)


def market_guess(ticker):
    if not ticker or ticker in PRIVATE_TICKERS:
        return "PRIVATE"
    if re.fullmatch(r"\d{6}", ticker):
        return "CN"
    for suffix, market in MARKET_BY_SUFFIX.items():
        if ticker.endswith(suffix):
            return market
    if re.fullmatch(r"[A-Z][A-Z0-9]{0,9}", ticker):
        return "US_LIKE"
    return "UNKNOWN"


def is_a_share(ticker):
    return market_guess(ticker) == "CN"


def canonical_segment(slug, name):
    if name in CANONICAL_SEGMENT_ALIASES:
        return CANONICAL_SEGMENT_ALIASES[name], name
    return slug, name


def build_universe(source_path):
    data = json.loads(source_path.read_text(encoding="utf-8"))
    source_segments = [x for x in data.get("entities", []) if x.get("type") == "segment"]

    grouped = defaultdict(list)
    for segment in source_segments:
        segment_id, canonical_name = canonical_segment(segment.get("slug"), segment.get("name"))
        grouped[segment_id].append((segment, canonical_name))

    segments = []
    for segment_id, rows in grouped.items():
        first = rows[0][0]
        name = rows[0][1] or segment_id
        industries = []
        source_slugs = []
        companies = {}

        for row, _ in rows:
            _row_inds = row.get("industries") or ([row.get("industry")] if row.get("industry") else [])
            for industry in _row_inds:
                if industry and industry not in industries:
                    industries.append(industry)
            source_slugs.append(row.get("slug"))

            for raw in row.get("companies") or []:
                original_ticker = str(raw.get("ticker") or "").strip().upper()
                ticker = normalize_ticker(original_ticker)
                if not ticker:
                    continue

                market = market_guess(ticker)
                tradable = ticker not in PRIVATE_TICKERS
                item = companies.setdefault(ticker, {
                    "ticker": ticker,
                    "source_tickers": [],
                    "name": raw.get("name"),
                    "roles": [],
                    "rev": None,
                    "market_guess": market,
                    "tradable": tradable,
                    "in_overseas_heat": tradable and market != "CN",
                })
                if original_ticker and original_ticker not in item["source_tickers"]:
                    item["source_tickers"].append(original_ticker)
                if raw.get("name") and not item.get("name"):
                    item["name"] = raw.get("name")
                role = raw.get("role")
                if role and role not in item["roles"]:
                    item["roles"].append(role)
                rev = raw.get("rev")
                if isinstance(rev, (int, float)) and (item.get("rev") is None or rev > item["rev"]):
                    item["rev"] = round(float(rev), 2)

        overseas = [x for x in companies.values() if x["in_overseas_heat"]]
        a_share = [x for x in companies.values() if is_a_share(x["ticker"])]
        segments.append({
            "segment_id": segment_id,
            "name": name,
            "industry_tags": industries,
            "layer": first.get("layer"),
            "source_slugs": sorted(source_slugs),
            "description": first.get("description"),
            "chain_note": first.get("description"),
            "companies": sorted(companies.values(), key=lambda x: x["ticker"]),
            "n_source_companies": sum(len(row.get("companies") or []) for row, _ in rows),
            "n_unique_companies": len(companies),
            "n_overseas_candidates": len(overseas),
            "n_a_share_mapping": len(a_share),
            "a_share": [
                {"name": x["name"], "ticker": x["ticker"], "role": "; ".join(x["roles"])}
                for x in sorted(a_share, key=lambda x: x["ticker"])
            ],
        })

    segments.sort(key=lambda x: (x["industry_tags"][0] if x["industry_tags"] else "", x["name"]))

    all_companies = {}
    for segment in segments:
        for company in segment["companies"]:
            item = all_companies.setdefault(company["ticker"], {
                "ticker": company["ticker"],
                "name": company["name"],
                "market_guess": company["market_guess"],
                "tradable": company["tradable"],
                "segments": [],
            })
            item["segments"].append(segment["segment_id"])
    for company in all_companies.values():
        company["segments"] = sorted(set(company["segments"]))

    overseas = [x for x in all_companies.values() if x["tradable"] and x["market_guess"] != "CN"]
    stats = {
        "source_segments": len(source_segments),
        "canonical_segments": len(segments),
        "merged_exact_duplicate_records": len(source_segments) - len(segments),
        "source_company_links": sum(len(row.get("companies") or []) for row in source_segments),
        "unique_companies": len(all_companies),
        "overseas_quote_candidates": len(overseas),
        "a_share_mapping_companies": sum(
            1 for x in all_companies.values() if x["market_guess"] == "CN"
        ),
        "private_or_untradable": sum(1 for x in all_companies.values() if not x["tradable"]),
    }

    return {
        "source_type": "invest_wiki",
        "source_file": "L3-网页产物/wiki_data.json",
        "note": (
            "Canonical segments merge exact cross-track duplicate names. "
            "Overseas quote candidates exclude A-shares and known private companies."
        ),
        "stats": stats,
        "segments": segments,
        "companies": dict(sorted(all_companies.items())),
    }


def source_commit():
    try:
        return subprocess.check_output(
            # ":/" 前缀让 pathspec 相对仓库根解析，不随 cwd 变化
            ["git", "log", "-1", "--format=%H", "--", ":/L3-网页产物/wiki_data.json"],
            cwd=SCRIPT_DIR,
            text=True,
        ).strip()
    except Exception:
        return None


def source_is_dirty():
    try:
        result = subprocess.check_output(
            # ":/" 前缀让 pathspec 相对仓库根解析。原先用 "L2-Wiki" 这类仓库根相对路径
            # 配合 cwd=SCRIPT_DIR(L3-网页产物)，pathspec 一个都匹配不到 → 恒返回空 → dirty 恒为 False
            ["git", "status", "--porcelain", "--", ":/L2-Wiki", ":/L3-网页产物/wiki_data.json"],
            cwd=SCRIPT_DIR,
            text=True,
        )
        return bool(result.strip())
    except Exception:
        return None


def next_version(output_path):
    now = datetime.datetime.now().astimezone()
    today = now.date().isoformat()
    sequence = 1
    try:
        old = json.loads(output_path.read_text(encoding="utf-8"))
        match = re.fullmatch(rf"{re.escape(today)}\.(\d+)", str(old.get("version", "")))
        if match:
            sequence = int(match.group(1)) + 1
    except (OSError, ValueError, json.JSONDecodeError):
        pass
    return f"{today}.{sequence}"


def add_metadata(universe, source_path, output_path):
    source_bytes = source_path.read_bytes()
    source_sha256 = hashlib.sha256(source_bytes).hexdigest()
    commit = source_commit()
    dirty = source_is_dirty()
    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    universe["version"] = next_version(output_path)
    universe["logic_version"] = LOGIC_VERSION
    universe["built_at"] = now
    universe["source_generated_at"] = datetime.datetime.fromtimestamp(
        source_path.stat().st_mtime
    ).astimezone().isoformat(timespec="seconds")
    universe["source_sha256"] = source_sha256
    universe["source_hash8"] = source_sha256[:8]
    universe["source_commit"] = commit
    universe["source_dirty"] = dirty
    return universe


def validate(universe):
    stats = universe.get("stats", {})
    if stats.get("source_segments", 0) <= 0:
        raise ValueError("no source segments found")
    if stats.get("canonical_segments", 0) <= 0:
        raise ValueError("no canonical segments generated")
    if stats.get("unique_companies", 0) <= 0:
        raise ValueError("no companies generated")
    segment_ids = [x["segment_id"] for x in universe["segments"]]
    if len(segment_ids) != len(set(segment_ids)):
        raise ValueError("duplicate canonical segment_id")


def main():
    args = sys.argv[1:]
    if any(arg in ("-h", "--help") for arg in args):
        print(__doc__)
        return 0
    input_path = Path(args[0]).resolve() if len(args) > 0 else DEFAULT_INPUT
    output_path = Path(args[1]).resolve() if len(args) > 1 else DEFAULT_OUTPUT

    universe = build_universe(input_path)
    validate(universe)
    add_metadata(universe, input_path, output_path)
    output_path.write_text(
        json.dumps(universe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(json.dumps({
        "version": universe["version"],
        "logic_version": universe["logic_version"],
        "source_sha256": universe["source_sha256"],
        "source_commit": universe["source_commit"],
        "source_dirty": universe["source_dirty"],
        **universe["stats"],
    }, ensure_ascii=False, indent=2))
    print(f"output: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
