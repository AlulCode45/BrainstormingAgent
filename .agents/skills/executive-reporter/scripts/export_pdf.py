#!/usr/bin/env python3
"""Export a Markdown report or PRP folder to a clean, print-ready PDF.

Uses only Python stdlib + headless Chromium (Brave / Chrome) --print-to-pdf.
Usage:
  python3 export_pdf.py --input report.md --output report.pdf [--title "Title"]
  python3 export_pdf.py --project prps/<slug> --output prps/<slug>/assets/report.pdf
"""
import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

BROWSER_CANDIDATES = [
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome"),
    shutil.which("chromium"),
    shutil.which("brave-browser"),
]

PRP_SECTION_ORDER = [
    "18-executive-summary.md",
    "17-scorecard-and-decision.md",
    "00-overview.md",
    "07-market-research.md",
    "15-competitor-analysis.md",
    "14-customer-discovery.md",
    "08-swot.md",
    "09-opportunity-analysis.md",
    "10-management-plan.md",
    "11-financial-plan.md",
    "16-compliance-and-legal.md",
    "12-go-to-market-and-risk.md",
    "13-assumption-register.md",
]

CSS = """
@page {
  size: A4;
  margin: 20mm 18mm 20mm 18mm;
  @bottom-left {
    content: string(doc-title);
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
    font-size: 8pt;
    color: #6B7280;
  }
  @bottom-right {
    content: "Halaman " counter(page) " dari " counter(pages);
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
    font-size: 8pt;
    color: #6B7280;
  }
}
@page :first {
  @bottom-left { content: none; }
}
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
  font-size: 10pt;
  line-height: 1.55;
  color: #1A1D21;
  margin: 0;
  padding: 0;
  background: #FFFFFF;
}
.doc-header {
  border-bottom: 2px solid #1B365D;
  padding-bottom: 12px;
  margin-bottom: 20px;
}
.doc-kicker {
  font-size: 8.5pt;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #1B365D;
  margin: 0 0 6px 0;
}
.doc-title {
  string-set: doc-title content();
  font-size: 20pt;
  font-weight: 700;
  line-height: 1.2;
  color: #111317;
  margin: 0 0 8px 0;
}
.doc-meta {
  font-size: 8.5pt;
  color: #525866;
  margin: 0;
}
h1 {
  font-size: 15pt;
  font-weight: 700;
  color: #111317;
  border-bottom: 1px solid #D9DEE5;
  padding-bottom: 4px;
  margin: 24px 0 10px 0;
  break-after: avoid;
}
h2 {
  font-size: 12pt;
  font-weight: 700;
  color: #1B365D;
  margin: 18px 0 8px 0;
  break-after: avoid;
}
h3 {
  font-size: 10.5pt;
  font-weight: 600;
  color: #1A1D21;
  margin: 14px 0 6px 0;
  break-after: avoid;
}
p { margin: 0 0 9px 0; }
ul, ol { margin: 0 0 10px 0; padding-left: 18px; }
li { margin-bottom: 4px; }
blockquote {
  margin: 12px 0;
  padding: 10px 14px;
  background: #F7F8FA;
  border-left: 3px solid #1B365D;
  color: #2C313A;
  font-size: 9.5pt;
  break-inside: avoid;
}
blockquote p:last-child { margin-bottom: 0; }
table {
  width: 100%;
  border-collapse: collapse;
  margin: 12px 0 16px 0;
  font-size: 9pt;
  break-inside: avoid;
}
th {
  background: #F4F6F8;
  color: #111317;
  font-weight: 600;
  text-align: left;
  padding: 7px 8px;
  border-top: 1.5px solid #1B365D;
  border-bottom: 1px solid #B8C0CC;
}
td {
  padding: 6px 8px;
  border-bottom: 1px solid #E5E8ED;
  vertical-align: top;
}
tr:last-child td { border-bottom: 1px solid #B8C0CC; }
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }
code {
  font-family: "SF Mono", Menlo, Monaco, Consolas, monospace;
  font-size: 8.5pt;
  background: #F4F6F8;
  padding: 1px 4px;
  border-radius: 2px;
}
pre {
  background: #F7F8FA;
  border: 1px solid #E5E8ED;
  padding: 10px 12px;
  font-size: 8.5pt;
  overflow-x: auto;
  break-inside: avoid;
}
pre code { background: none; padding: 0; }
hr {
  border: 0;
  border-top: 1px solid #D9DEE5;
  margin: 18px 0;
}
img, svg {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 12px auto;
  break-inside: avoid;
}
.tag {
  font-family: "SF Mono", Menlo, monospace;
  font-size: 7.5pt;
  padding: 1px 4px;
  border: 1px solid #C7CFD9;
  color: #374151;
  background: #F9FAFB;
  border-radius: 2px;
  white-space: nowrap;
}
.page-break { break-before: page; }
a { color: #1B365D; text-decoration: none; }
"""


def find_browser() -> str:
    for path in BROWSER_CANDIDATES:
        if path and os.path.exists(path):
            return path
    raise RuntimeError("No Chromium-based browser (Brave/Chrome) found for PDF export.")


def format_inline(text: str) -> str:
    # Preserve raw inline <svg>...</svg> untouched if present
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(
        r"\[(Verified|Estimate|Assumption|Unverified|Contoh)\]",
        r'<span class="tag">\1</span>',
        text,
    )
    return text


def is_numeric_cell(cell: str) -> bool:
    s = cell.strip().replace(",", "").replace(".", "").replace("%", "").replace("+", "").replace("-", "")
    return bool(s) and s.isdigit()


def md_to_html(md_text: str, base_dir: Path) -> str:
    lines = md_text.splitlines()
    out = []
    i = 0
    in_ul = False
    in_ol = False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Raw SVG block passthrough
        if stripped.startswith("<svg"):
            close_lists()
            svg_lines = [line]
            while i + 1 < len(lines) and "</svg>" not in lines[i]:
                i += 1
                svg_lines.append(lines[i])
            out.append("\n".join(svg_lines))
            i += 1
            continue

        # Page break marker
        if stripped == "<!-- pagebreak -->":
            close_lists()
            out.append('<div class="page-break"></div>')
            i += 1
            continue

        # Fenced code block
        if stripped.startswith("```"):
            close_lists()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(html.escape(lines[i]))
                i += 1
            out.append("<pre><code>" + "\n".join(code_lines) + "</code></pre>")
            i += 1
            continue

        # Blank line
        if not stripped:
            close_lists()
            i += 1
            continue

        # Horizontal rule
        if stripped in ("---", "***", "___"):
            close_lists()
            out.append("<hr>")
            i += 1
            continue

        # Headings
        m = re.match(r"^(#{1,3})\s+(.*)$", stripped)
        if m:
            close_lists()
            level = len(m.group(1))
            out.append(f"<h{level}>{format_inline(m.group(2))}</h{level}>")
            i += 1
            continue

        # Image
        img_m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", stripped)
        if img_m:
            close_lists()
            alt = html.escape(img_m.group(1))
            src = img_m.group(2)
            if not src.startswith(("http://", "https://", "file://", "/")):
                src = (base_dir / src).resolve().as_uri()
            out.append(f'<img src="{src}" alt="{alt}">')
            i += 1
            continue

        # Markdown table
        if "|" in stripped and i + 1 < len(lines) and re.match(r"^\|?[\s:|-]+\|[\s:|-]*$", lines[i + 1].strip()):
            close_lists()
            headers = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and "|" in lines[i].strip():
                row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(row)
                i += 1
            # Detect numeric columns
            num_cols = set()
            for col_idx in range(len(headers)):
                if rows and all(col_idx < len(r) and is_numeric_cell(r[col_idx]) for r in rows):
                    num_cols.add(col_idx)
            tbl = ["<table><thead><tr>"]
            for idx, h in enumerate(headers):
                cls = ' class="num"' if idx in num_cols else ""
                tbl.append(f"<th{cls}>{format_inline(h)}</th>")
            tbl.append("</tr></thead><tbody>")
            for r in rows:
                tbl.append("<tr>")
                for idx in range(len(headers)):
                    val = r[idx] if idx < len(r) else ""
                    cls = ' class="num"' if idx in num_cols else ""
                    tbl.append(f"<td{cls}>{format_inline(val)}</td>")
                tbl.append("</tr>")
            tbl.append("</tbody></table>")
            out.append("".join(tbl))
            continue

        # Blockquote
        if stripped.startswith(">"):
            close_lists()
            bq_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                bq_lines.append(format_inline(lines[i].strip().lstrip(">").strip()))
                i += 1
            out.append("<blockquote><p>" + "<br>".join(bq_lines) + "</p></blockquote>")
            continue

        # Unordered list
        ul_m = re.match(r"^[-*]\s+(.*)$", stripped)
        if ul_m:
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            raw_item = ul_m.group(1)
            prefix = ""
            if re.match(r"^\[ \]\s+", raw_item):
                raw_item = re.sub(r"^\[ \]\s+", "", raw_item)
                prefix = "&#9744; "
            elif re.match(r"^\[x\]\s+", raw_item, flags=re.I):
                raw_item = re.sub(r"^\[x\]\s+", "", raw_item, flags=re.I)
                prefix = "&#9745; "
            out.append(f"<li>{prefix}{format_inline(raw_item)}</li>")
            i += 1
            continue

        # Ordered list
        ol_m = re.match(r"^\d+\.\s+(.*)$", stripped)
        if ol_m:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{format_inline(ol_m.group(1))}</li>")
            i += 1
            continue

        # Paragraph
        close_lists()
        para = [stripped]
        while (
            i + 1 < len(lines)
            and lines[i + 1].strip()
            and not re.match(r"^(#{1,3}\s|[-*]\s|\d+\.\s|>|```|---|\*\*\*|<svg|<!--)", lines[i + 1].strip())
            and "|" not in lines[i + 1]
        ):
            i += 1
            para.append(lines[i].strip())
        out.append(f"<p>{format_inline(' '.join(para))}</p>")
        i += 1

    close_lists()
    return "\n".join(out)


def load_project_markdown(project_dir: Path) -> str:
    parts = []
    for fname in PRP_SECTION_ORDER:
        p = project_dir / fname
        if p.exists():
            parts.append(p.read_text(encoding="utf-8").strip())
    if not parts:
        raise FileNotFoundError(f"No PRP markdown files found in {project_dir}")
    return "\n\n<!-- pagebreak -->\n\n".join(parts)


def build_html(body_html: str, title: str, kicker: str, meta: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<header class="doc-header">
  <p class="doc-kicker">{html.escape(kicker)}</p>
  <h1 class="doc-title" style="border:none;margin:0 0 6px 0;padding:0;">{html.escape(title)}</h1>
  <p class="doc-meta">{html.escape(meta)}</p>
</header>
{body_html}
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description="Export Markdown or PRP folder to PDF.")
    ap.add_argument("--input", help="Path to a Markdown file")
    ap.add_argument("--project", help="Path to a prps/<project> folder")
    ap.add_argument("--output", required=True, help="Output PDF path")
    ap.add_argument("--title", help="Document title")
    ap.add_argument("--kicker", default="Strategic Analysis Report", help="Top label above title")
    ap.add_argument("--meta", default=f"Tanggal: {date.today().isoformat()}", help="Subtitle metadata")
    args = ap.parse_args()

    if not args.input and not args.project:
        ap.error("Provide either --input or --project.")

    if args.input:
        in_path = Path(args.input).resolve()
        md_text = in_path.read_text(encoding="utf-8")
        base_dir = in_path.parent
        default_title = in_path.stem.replace("-", " ").title()
    else:
        proj_dir = Path(args.project).resolve()
        md_text = load_project_markdown(proj_dir)
        base_dir = proj_dir
        default_title = proj_dir.name.replace("-", " ").title()

    title = args.title or default_title
    body_html = md_to_html(md_text, base_dir)
    full_html = build_html(body_html, title, args.kicker, args.meta)

    out_path = Path(args.output).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    browser = find_browser()
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tmp:
        tmp.write(full_html)
        tmp_path = Path(tmp.name)

    try:
        cmd = [
            browser,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={out_path}",
            tmp_path.as_uri(),
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if res.returncode != 0 or not out_path.exists():
            print(res.stderr, file=sys.stderr)
            sys.exit(1)
        print(f"PDF generated: {out_path} ({out_path.stat().st_size:,} bytes)")
    finally:
        tmp_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
