#!/usr/bin/env python3
"""
invest_wiki 文章保存器 — 抓取网页全文 + 下载图片到本地

用法：
  python3 engine/save_article.py <url> --output-dir L0-原始资料池/_attachments/

流程：
  1. 调 web-fetch/dispatch.py 抓取 Markdown 全文
  2. 提取所有 ![](url) 图片链接
  3. 下载图片到 <output_dir>/images/
  4. 替换 Markdown 中的远程 URL 为本地相对路径
  5. 输出 Markdown 文件名
"""

import sys
import os
import re
import json
import hashlib
import subprocess
import argparse
import time
import urllib.request
from pathlib import Path
from urllib.parse import urlparse, urljoin

SKILL_DIR = Path.home() / ".claude/skills/web-fetch"
DISPATCH_PY = SKILL_DIR / "dispatch.py"

# 图片下载的 User-Agent（避免被图片服务器拒绝）
IMG_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Referer": "https://mp.weixin.qq.com/",
}


def extract_image_urls(markdown_text):
    """从 Markdown 中提取所有图片 URL"""
    # 匹配 ![alt](url) 和 ![](url)
    pattern = r'!\[[^\]]*\]\(([^)\s]+)\)'
    urls = re.findall(pattern, markdown_text)
    # 去重保持顺序
    seen = set()
    unique = []
    for u in urls:
        if u not in seen and not u.startswith("data:"):
            seen.add(u)
            unique.append(u)
    return unique


def download_image(url, save_dir, timeout=15):
    """下载单张图片，返回本地文件名。失败返回 None。"""
    try:
        # 从 URL 生成唯一文件名
        url_hash = hashlib.md5(url.encode()).hexdigest()[:10]

        # 尝试从 URL 提取原始扩展名
        parsed = urlparse(url)
        path = parsed.path
        ext_match = re.search(r'wx_fmt=(\w+)', url)
        if ext_match:
            ext = "." + ext_match.group(1)
        elif path and "." in path.split("/")[-1]:
            ext = "." + path.split("/")[-1].rsplit(".", 1)[1].split("?")[0]
            ext = "." + ext[:4]  # 限制长度
        else:
            ext = ".jpg"  # 默认

        filename = f"{url_hash}{ext}"
        filepath = save_dir / filename

        # 已存在则跳过
        if filepath.exists():
            return filename

        req = urllib.request.Request(url, headers=IMG_HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            if len(data) < 100:
                return None
            filepath.write_bytes(data)
            return filename

    except Exception as e:
        print(f"  [WARN] 图片下载失败: {url[:80]}... — {e}", file=sys.stderr)
        return None


def save_article(url, output_dir, max_chars=100000, timeout=30):
    """
    抓取文章全文 + 下载图片，保存到 output_dir。

    返回: (markdown_filepath, image_count, stats_dict)
    """
    out_dir = Path(output_dir).resolve()
    img_dir = out_dir / "images"
    img_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: 抓取 Markdown
    if not DISPATCH_PY.exists():
        raise FileNotFoundError(f"dispatch.py not found at {DISPATCH_PY}")

    print(f"📡 抓取: {url}", file=sys.stderr)
    result = subprocess.run(
        ["python3", str(DISPATCH_PY), url, "--max-chars", str(max_chars),
         "--timeout", str(timeout)],
        capture_output=True, text=True, timeout=timeout + 30
    )

    # dispatch.py 成功时直接输出到 stdout，失败时 JSON 到 stderr
    content = result.stdout.strip()
    if not content or len(content) < 200:
        # 尝试从 stderr 解析 JSON 错误
        try:
            err = json.loads(result.stderr.strip())
            raise RuntimeError(f"抓取失败: {err.get('error', result.stderr[:300])}")
        except json.JSONDecodeError:
            raise RuntimeError(f"抓取失败: 内容太短 ({len(content)} chars)")

    print(f"✅ 抓取成功: {len(content)} 字符", file=sys.stderr)

    # Step 2: 提取图片
    image_urls = extract_image_urls(content)
    print(f"🖼  发现 {len(image_urls)} 张图片", file=sys.stderr)

    # Step 3: 下载图片并替换 URL
    downloaded = 0
    failed = 0
    replacements = {}

    for i, img_url in enumerate(image_urls):
        local_name = download_image(img_url, img_dir)
        if local_name:
            replacements[img_url] = f"images/{local_name}"
            downloaded += 1
            if (downloaded) % 5 == 0:
                print(f"  已下载 {downloaded}/{len(image_urls)} ...", file=sys.stderr)
        else:
            failed += 1

    # Step 4: 替换 Markdown 中的图片 URL
    modified_content = content
    for remote_url, local_path in replacements.items():
        # 转义特殊字符用于正则替换
        escaped = re.escape(remote_url)
        modified_content = re.sub(
            r'!\[([^\]]*)\]\(' + escaped + r'\)',
            f'![]({local_path})',
            modified_content
        )

    # Step 5: 生成文件名并保存
    timestamp = time.strftime("%Y-%m-%d")
    domain = urlparse(url).netloc.replace(".", "-") or "web"

    # 尝试从 Markdown 一级标题提取
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
        safe_title = re.sub(r'[^\w\s一-鿿-]', '', title).strip()
        safe_title = safe_title[:40] if len(safe_title) > 60 else safe_title
        markdown_filename = f"{timestamp}-{safe_title}-原文.md"
    else:
        # 无标题 → 用域名+hash 保证唯一
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        markdown_filename = f"{timestamp}-{domain}-{url_hash}-原文.md"
    markdown_path = out_dir / markdown_filename

    markdown_path.write_text(modified_content, encoding="utf-8")

    stats = {
        "url": url,
        "content_chars": len(content),
        "image_urls_found": len(image_urls),
        "images_downloaded": downloaded,
        "images_failed": failed,
        "local_images_dir": str(img_dir),
        "markdown_file": str(markdown_path),
    }

    print(f"📄 保存: {markdown_path} ({len(modified_content)} 字符)", file=sys.stderr)
    print(f"🖼  图片: {downloaded} 下载 / {failed} 失败 → {img_dir}", file=sys.stderr)

    return markdown_path, downloaded, stats


def main():
    parser = argparse.ArgumentParser(
        description="invest_wiki 文章保存器 — 抓取网页全文 + 下载图片到本地",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python3 engine/save_article.py https://mp.weixin.qq.com/s/xxx \\
      --output-dir L0-原始资料池/_attachments/

输出:
  - L0-原始资料池/_attachments/2026-07-27-文章标题-原文.md
  - L0-原始资料池/_attachments/images/  (全部图片)
        """
    )
    parser.add_argument("url", help="目标 URL")
    parser.add_argument("--output-dir", required=True,
                        help="输出目录（Markdown + images/ 子目录）")
    parser.add_argument("--max-chars", type=int, default=100000,
                        help="最大字符数 (default: 100000)")
    parser.add_argument("--timeout", type=int, default=45,
                        help="抓取超时秒数 (default: 45)")

    args = parser.parse_args()

    try:
        md_path, img_count, stats = save_article(
            args.url, args.output_dir,
            max_chars=args.max_chars, timeout=args.timeout
        )
        # 输出 JSON 给调用方
        print(json.dumps(stats, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"ok": False, "error": str(e)}, indent=2, ensure_ascii=False),
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
