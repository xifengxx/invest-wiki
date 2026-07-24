#!/usr/bin/env python3
"""Invest Wiki — 数据新鲜度扫描器

Phase 3 核心工具：扫描 wiki_data.json 中所有公司，检查 data_freshness_date 字段，
标记超过 STALE_DAYS 天未更新的条目，输出报告。

使用方式:
    python L3-网页产物/freshness_scan.py           # 默认 90 天阈值
    python L3-网页产物/freshness_scan.py --days 60  # 自定义阈值
    python L3-网页产物/freshness_scan.py --json     # JSON 输出（供 CI/自动化使用）
"""

import json
import sys
import os
from datetime import datetime, date

STALE_DAYS = 90
WARN_DAYS = 60  # 预警阈值（接近过期）

# 财报季月份：大批公司更新财务数据的时间窗口
EARNINGS_MONTHS = {1, 4, 7, 10}


def parse_date(date_val) -> date | None:
    """解析 data_freshness_date 字段，支持字符串/date对象/多种格式。"""
    if date_val is None:
        return None
    # 如果 YAML 解析器已经将其转为 Python date 对象
    if isinstance(date_val, date):
        return date_val
    if isinstance(date_val, datetime):
        return date_val.date()
    if not isinstance(date_val, str):
        return None
    if not date_val.strip():
        return None
    date_str = date_val.strip()
    formats = [
        '%Y-%m-%d',
        '%Y-%m',
        '%Y/%m/%d',
        '%Y/%m',
    ]
    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.date()
        except ValueError:
            continue
    # 尝试只解析年份-月份（如 "2026-07"）
    import re
    m = re.match(r'(\d{4})-(\d{2})', date_str)
    if m:
        return date(int(m.group(1)), int(m.group(2)), 1)
    return None


def parse_market_cap_date(mcap_str: str) -> date | None:
    """尝试从 market_cap 字段中提取日期。例如 '~$100B（2026.7）'"""
    if not mcap_str:
        return None
    import re
    # 匹配中文括号中的日期
    m = re.search(r'[（(](\d{4})[./年](\d{1,2})[月)）]', mcap_str)
    if m:
        return date(int(m.group(1)), int(m.group(2)), 1)
    # 匹配英文括号
    m = re.search(r'\((\d{4})[-./](\d{1,2})\)', mcap_str)
    if m:
        return date(int(m.group(1)), int(m.group(2)), 1)
    return None


def freshness_label(days_old: int) -> str:
    if days_old < 0:
        return '🟢'  # 数据日期在未来（可能是笔误）
    elif days_old <= 30:
        return '🟢 新鲜'
    elif days_old <= WARN_DAYS:
        return '🟡 预警'
    elif days_old <= STALE_DAYS:
        return '🟠 即将过期'
    else:
        return '🔴 已过期'


def scan(data_path: str, stale_days: int = STALE_DAYS) -> dict:
    """扫描 wiki_data.json，返回新鲜度报告。"""
    with open(data_path) as f:
        data = json.load(f)

    companies = [e for e in data['entities'] if e.get('type') == 'company']
    today = date.today()

    results = {
        'scan_date': today.isoformat(),
        'total_companies': len(companies),
        'stale_threshold_days': stale_days,
        'fresh': [],       # data_freshness_date 存在且未过期
        'stale': [],        # 超过阈值
        'missing': [],      # 没有 data_freshness_date 字段
        'warn': [],         # 预警中（接近过期）
        'earnings_season': today.month in EARNINGS_MONTHS,
    }

    for c in companies:
        name = c.get('name', '?')
        slug = c.get('slug', '?')
        dfs_str = c.get('data_freshness_date', '')
        mcap_str = c.get('market_cap', '')

        dfs_date = parse_date(dfs_str)

        entry = {
            'slug': slug,
            'name': name,
            'data_freshness_date': dfs_str,
            'market_cap': (mcap_str or '')[:60],
            'ticker': c.get('ticker', ''),
            'has_market_cap': bool(mcap_str and mcap_str.strip()),
        }

        if not dfs_date:
            # 没有 freshness 字段，但有 market_cap（说明是深度覆盖公司）
            if entry['has_market_cap']:
                # 尝试从 market_cap 字符串中提取日期作为近似值
                mcap_date = parse_market_cap_date(mcap_str)
                if mcap_date:
                    days = (today - mcap_date).days
                    entry['approx_date'] = mcap_date.isoformat()
                    entry['days_old'] = days
                    if days > stale_days:
                        results['stale'].append(entry)
                    else:
                        entry['label'] = '⚠️ 无data_freshness_date，从market_cap估算'
                        results['warn'].append(entry)
                else:
                    entry['label'] = '❌ 深度覆盖但缺少data_freshness_date'
                    results['missing'].append(entry)
            continue

        days_old = (today - dfs_date).days
        entry['days_old'] = days_old
        entry['label'] = freshness_label(days_old)

        if days_old > stale_days:
            results['stale'].append(entry)
        elif days_old > WARN_DAYS:
            results['warn'].append(entry)
        else:
            results['fresh'].append(entry)

    # Sort stale by oldest first
    results['stale'].sort(key=lambda x: x.get('days_old', 0), reverse=True)
    results['warn'].sort(key=lambda x: x.get('days_old', 0), reverse=True)

    return results


def print_report(results: dict):
    """打印人类可读的新鲜度报告。"""
    print("=" * 65)
    print("  Invest Wiki — 数据新鲜度扫描报告")
    print(f"  扫描日期: {results['scan_date']}")
    print(f"  总词条数: {results['total_companies']}")
    print(f"  过期阈值: {results['stale_threshold_days']} 天")
    print(f"  财报季: {'🔔 是（' + '/'.join(str(m) for m in EARNINGS_MONTHS) + '月）' if results['earnings_season'] else '否'}")
    print("=" * 65)

    fresh_count = len(results['fresh'])
    warn_count = len(results['warn'])
    stale_count = len(results['stale'])
    missing_count = len(results['missing'])

    print(f"\n  🟢 新鲜: {fresh_count} 条")
    print(f"  🟡 预警: {warn_count} 条")
    print(f"  🔴 过期: {stale_count} 条")
    print(f"  ⚠️  缺失: {missing_count} 条")

    if results['stale']:
        print(f"\n  {'─' * 55}")
        print(f"  🔴 过期条目（>{results['stale_threshold_days']}天未更新）:")
        for e in results['stale']:
            print(f"     {e['days_old']:4d}d ago — {e['name'][:30]:30s} {e.get('ticker',''):12s}  freshness={e.get('data_freshness_date','?')}")

    if results['warn']:
        print(f"\n  {'─' * 55}")
        print(f"  🟡 预警条目（>{WARN_DAYS}天，即将过期）:")
        for e in results['warn']:
            print(f"     {e['days_old']:4d}d ago — {e['name'][:30]:30s} {e.get('ticker',''):12s}  freshness={e.get('data_freshness_date','?')}")

    if results['missing']:
        print(f"\n  {'─' * 55}")
        print(f"  ⚠️  缺失条目（深度覆盖但无 data_freshness_date）:")
        for e in results['missing']:
            print(f"     {e['name'][:40]:40s} mcap={(e.get('market_cap') or '?')[:40]}")

    print(f"\n  {'─' * 55}")
    if stale_count == 0 and missing_count == 0:
        print(f"  ✅ 数据新鲜度健康 — 所有深度覆盖公司均在 {results['stale_threshold_days']} 天内更新")
    else:
        print(f"  ❌ 需要刷新 {stale_count + missing_count} 个条目")
        if results['earnings_season']:
            print(f"  💡 当前为财报季，建议立即执行刷新操作")

    print()


def main():
    stale_days = STALE_DAYS
    json_output = False

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--days' and i + 1 < len(args):
            stale_days = int(args[i + 1])
            i += 2
        elif args[i] == '--json':
            json_output = True
            i += 1
        else:
            i += 1

    # 确定 wiki_data.json 路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'wiki_data.json')

    if not os.path.exists(data_path):
        print(f"❌ 找不到 wiki_data.json: {data_path}", file=sys.stderr)
        print("   请先运行: python L3-网页产物/build_wiki_data.py", file=sys.stderr)
        sys.exit(1)

    results = scan(data_path, stale_days)

    if json_output:
        print(json.dumps(results, ensure_ascii=False, indent=2, default=str))
    else:
        print_report(results)

    # 返回退出码
    if results['stale'] or results['missing']:
        sys.exit(1)


if __name__ == '__main__':
    main()
