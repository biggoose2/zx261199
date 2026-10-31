"""把 jellyfrog.html 里引用的 assets/*.webp 内嵌成 data URI，生成可直接双击打开的单文件版 dist/jellyfrog.html。"""
import base64, pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
html = (root / 'jellyfrog.html').read_text(encoding='utf-8')

def inline(m):
    data = (root / m.group(0)).read_bytes()
    return 'data:image/webp;base64,' + base64.b64encode(data).decode()

out = re.sub(r'assets/[a-z_]+\.webp', inline, html)
(root / 'dist').mkdir(exist_ok=True)
(root / 'dist' / 'jellyfrog.html').write_text(out, encoding='utf-8')
print(f"dist/jellyfrog.html {len(out) // 1024} KB")
