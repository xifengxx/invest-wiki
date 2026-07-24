"""Wiki HTML 验证脚本——数据修改后运行此脚本检查完整性。"""
import json, re, sys, os

HTML = os.path.join(os.path.dirname(__file__), 'index.html')
errors = []

def check(condition, msg):
    if not condition: errors.append(f"❌ {msg}")
    else: print(f"  ✅ {msg}")

with open(HTML) as f: html = f.read()
print(f"📄 {HTML} ({len(html)//1024}KB)\n")

# 1. HTML structure (exclude script blocks for tag counting)
print("1. HTML结构")
html_static = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
divs_open = len(re.findall(r'<div\b', html_static))
divs_close = html_static.count('</div>')
check(divs_open == divs_close, f"div平衡: {divs_open}开/{divs_close}闭")
check('</body>' in html, "</body> 存在")
check('</html>' in html, "</html> 存在")

# 2. Script tags
print("\n2. Script标签")
scripts_open = len(re.findall(r'<script[^>]*>', html))
scripts_close = html.count('</script>')
check(scripts_open == scripts_close, f"script平衡: {scripts_open}/{scripts_close}")

# 3. JSON data integrity (check wiki_data.json on disk)
print("\n3. 数据完整性")
data_path = os.path.join(os.path.dirname(__file__), 'wiki_data.json')
if os.path.exists(data_path):
    with open(data_path) as df:
        data = json.load(df)
    total = data.get('total', len(data.get('entities', [])))
    check(total > 400, f"词条数>400: {total}")
    segs = [e for e in data['entities'] if e['type'] == 'segment']
    check(len(segs) >= 74, f"赛道数≥74: {len(segs)}")
    wl = sum(1 for e in segs if len(e.get('wikilinks', [])) > 0)
    check(wl >= 60, f"有关联词条的赛道≥60: {wl}")
    check(len(data.get('hot', [])) >= 20, f"热力图≥20: {len(data.get('hot', []))}")
    # Check no unknown entities
    unknowns = [e for e in data['entities'] if e.get('type') == 'unknown']
    check(len(unknowns) == 0, f"无unknown实体: {len(unknowns)}个")
else:
    check(False, f"wiki_data.json不存在: {data_path}")

# 4. Key JS functions
print("\n4. JS关键函数")
for fn in ['buildTree', 'renderView', 'openDetail', 'closeDetail', 'doSearch']:
    check(f'function {fn}(' in html, f"函数 {fn}() 存在")

# Result
print(f"\n{'='*50}")
if errors:
    print(f"❌ 发现 {len(errors)} 个错误:")
    for e in errors: print(f"  {e}")
    sys.exit(1)
else:
    print("✅ 全部检查通过，可以安全打开")
    sys.exit(0)
