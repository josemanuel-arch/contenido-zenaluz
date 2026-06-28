#!/usr/bin/env python3
import sys, re, subprocess, os, pathlib
import markdown

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

# Quitar emojis (no hay fuente de emoji color); conservar flechas → (U+2192)
EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF☀-➿⬀-⯿⤴⤵️‍]",
    flags=re.UNICODE,
)

CSS = """
@page { size: A4; margin: 18mm 16mm 16mm 16mm; }
* { box-sizing: border-box; }
body { font-family: 'DejaVu Sans', 'Liberation Sans', sans-serif; font-size: 10.6pt;
       line-height: 1.5; color: #1a1a1a; }
h1 { font-size: 18pt; color: #5b2bd9; margin: 0 0 4px 0; line-height: 1.25;
     border-bottom: 3px solid #5b2bd9; padding-bottom: 8px; }
h2 { font-size: 13pt; color: #fff; background: #5b2bd9; padding: 6px 10px; border-radius: 6px;
     margin: 20px 0 10px 0; }
h3 { font-size: 11.5pt; color: #5b2bd9; margin: 14px 0 6px 0; }
p { margin: 6px 0; }
strong { color: #111; }
ul, ol { margin: 6px 0 6px 0; padding-left: 22px; }
li { margin: 3px 0; }
blockquote { margin: 6px 0; padding: 8px 12px; background: #f3eefe; border-left: 4px solid #5b2bd9;
             border-radius: 4px; font-style: normal; }
blockquote p { margin: 0; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 10pt; }
th, td { border: 1px solid #ccc; padding: 6px 8px; text-align: left; vertical-align: top; }
th { background: #ede7fb; color: #3a1a8c; }
code { font-family: 'DejaVu Sans Mono', monospace; background: #f1f1f4; padding: 1px 4px;
       border-radius: 3px; font-size: 9.2pt; }
pre { background: #1e1e2e; color: #eaeaea; padding: 12px 14px; border-radius: 8px; overflow: hidden;
      white-space: pre-wrap; word-wrap: break-word; font-size: 9pt; }
pre code { background: none; color: #eaeaea; padding: 0; }
hr { border: none; border-top: 1px solid #ddd; margin: 16px 0; }
.brandfoot { margin-top: 22px; padding-top: 8px; border-top: 1px solid #ddd; color: #888;
             font-size: 8.5pt; text-align: center; }
"""

def render(md_path, pdf_path):
    raw = pathlib.Path(md_path).read_text(encoding="utf-8")
    raw = EMOJI.sub("", raw)
    html_body = markdown.markdown(
        raw, extensions=["tables", "fenced_code", "sane_lists", "nl2br"]
    )
    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<style>{CSS}</style></head><body>{html_body}
<div class="brandfoot">Jomi · @jomia.ia — guion de rodaje · uso interno</div>
</body></html>"""
    html_path = str(pdf_path) + ".html"
    pathlib.Path(html_path).write_text(html, encoding="utf-8")
    cmd = [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
           "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
           "--virtual-time-budget=8000",
           f"--print-to-pdf={pdf_path}", "file://" + os.path.abspath(html_path)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if not os.path.exists(pdf_path) or os.path.getsize(pdf_path) < 1000:
        # reintento con --headless clásico
        cmd[1] = "--headless"
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    os.remove(html_path)
    ok = os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000
    print(("OK " if ok else "FALLO ") + pdf_path +
          (f" ({os.path.getsize(pdf_path)} bytes)" if ok else "\n" + r.stderr[-500:]))
    return ok

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2])
