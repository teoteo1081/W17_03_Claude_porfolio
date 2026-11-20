#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cấu hình dùng chung của Portfolio và CV (email, Zalo, GitHub, địa chỉ web công khai).

Nguồn: khối <script type="application/json" id="w17-site-config"> nằm GIỐNG HỆT NHAU trong hai file Final
(index.html = Portfolio, index_portfolio_clean.html = CV).

Đổi một giá trị (qua nút ⚙ Cài đặt trong editor -> POST /api/settings, hoặc lệnh dưới đây) sẽ:
  * thay giá trị CŨ bằng giá trị MỚI ở mọi chỗ trong cả hai file (href, chữ hiển thị, từ điển 4 ngôn ngữ,
    bản sửa đã nhúng), có ranh giới chặt để không đụng chuỗi dài hơn (vd. link repo github.com/<tên>/<repo> giữ nguyên);
  * đặt lại <link rel="canonical"> và og:url theo địa chỉ web công khai;
  * ghi khối cấu hình mới vào cả hai file.

Dùng:
    python tools/site_config.py --check    # kiểm hai file: khối cấu hình hợp lệ, giống nhau, canonical/og:url đúng
    python tools/site_config.py --show     # in cấu hình hiện tại
"""

import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PORTFOLIO = "index.html"
CV = "index_portfolio_clean.html"
FINALS = (PORTFOLIO, CV)
CV_PATH = "index_portfolio_clean.html"   # đường dẫn CV tính từ địa chỉ web gốc

SCHEMA = 1
CONFIG_RE = re.compile(r'(<script type="application/json" id="w17-site-config">)(.*?)(</script>)', re.S)
SETTINGS_SCRIPT_RE = re.compile(r'<script id="w17-settings-script">.*?</script>', re.S)
CANONICAL_RE = re.compile(r'<link rel="canonical" href="[^"]*">')
OG_URL_RE = re.compile(r'<meta property="og:url" content="[^"]*">')

# Các trường người dùng sửa được, theo đường dẫn trong JSON.
FIELDS = {
    "contact.email": {
        "re": re.compile(r"^[A-Za-z0-9._%+-]{1,64}@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,24}$"),
        "msg": "Email không hợp lệ (ví dụ: ten@gmail.com).",
        # ký tự có thể nằm sát trước/sau một địa chỉ email mà vẫn là một phần của chuỗi dài hơn
        "before": r"A-Za-z0-9._%+-", "after": r"A-Za-z0-9_-",
    },
    "contact.zaloUrl": {
        "re": re.compile(r"^https://zalo\.me/[A-Za-z0-9._-]{3,64}$"),
        "msg": "Link Zalo phải có dạng https://zalo.me/<số hoặc tên>.",
        "before": r"A-Za-z0-9._/-", "after": r"A-Za-z0-9_/-",
    },
    "contact.githubUrl": {
        "re": re.compile(r"^https://github\.com/[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$"),
        "msg": "Link GitHub phải có dạng https://github.com/<tên tài khoản> (không kèm tên repo).",
        # sau giá trị không được là '/', để link repo github.com/<tên>/<repo> không bị đổi theo
        "before": r"A-Za-z0-9._/-", "after": r"A-Za-z0-9_/-",
    },
    "site.baseUrl": {
        "re": re.compile(r"^https://[a-z0-9-]+(?:\.[a-z0-9-]+)+(?:/[A-Za-z0-9._~-]+)*/$"),
        "msg": "Địa chỉ web phải bắt đầu bằng https://, kết thúc bằng dấu /, không chứa ? # & hay khoảng trắng.",
    },
}
BLOCKED_HOSTS = ("localhost", "127.0.0.1", "0.0.0.0", "github.com", "www.github.com")


class ConfigError(Exception):
    """Cấu hình thiếu, hỏng hoặc giá trị mới không hợp lệ."""


def read(path):
    with io.open(path, encoding="utf-8", newline="") as fh:
        return fh.read()


def get(cfg, dotted):
    cur = cfg
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def _set(cfg, dotted, value):
    parts = dotted.split(".")
    cur = cfg
    for part in parts[:-1]:
        cur = cur.setdefault(part, {})
    cur[parts[-1]] = value


def json_for_script(obj):
    """Cùng cách thoát ký tự như w17JsonForScriptTag ở phía trình duyệt (không thể đóng thẻ <script> sớm)."""
    text = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return (text.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
            .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))


def validate_value(dotted, value):
    spec = FIELDS[dotted]
    if not isinstance(value, str):
        raise ConfigError(f"{dotted}: phải là chuỗi.")
    value = value.strip()
    if not spec["re"].match(value):
        raise ConfigError(spec["msg"])
    if dotted == "site.baseUrl":
        host = value.split("/")[2]
        if host in BLOCKED_HOSTS or host.startswith("127."):
            raise ConfigError("Địa chỉ web phải là trang công khai (vd. https://teoteo1081.github.io/W17_03_Claude_porfolio/), "
                              "không dùng localhost hay link repo GitHub.")
    return value


def validate_config(cfg):
    if not isinstance(cfg, dict) or cfg.get("schema") != SCHEMA:
        raise ConfigError(f"Khối w17-site-config phải là object có schema = {SCHEMA}.")
    for dotted in FIELDS:
        validate_value(dotted, get(cfg, dotted))
    return cfg


def parse_config(html):
    """Trả cấu hình trong một trang (None nếu trang không có khối cấu hình). Khối hỏng -> ConfigError."""
    found = CONFIG_RE.findall(html)
    if not found:
        return None
    if len(found) != 1:
        raise ConfigError("Trang có nhiều hơn một khối w17-site-config.")
    try:
        cfg = json.loads(found[0][1])
    except json.JSONDecodeError:
        raise ConfigError("Khối w17-site-config không phải JSON hợp lệ.")
    return validate_config(cfg)


def page_urls(cfg):
    base = cfg["site"]["baseUrl"]
    return {PORTFOLIO: base, CV: base + CV_PATH}


def _replace_bounded(text, old, new, spec):
    if old == new:
        return text, 0
    pattern = re.compile(f"(?<![{spec['before']}])" + re.escape(old) + f"(?![{spec['after']}])")
    return pattern.subn(lambda _m: new, text)


def apply_site_tags(html, name, cfg):
    """Đặt canonical (+ og:url nếu trang có thẻ đó) theo địa chỉ web công khai; thêm canonical nếu chưa có."""
    url = page_urls(cfg)[name]
    canonical = f'<link rel="canonical" href="{url}">'
    if CANONICAL_RE.search(html):
        html = CANONICAL_RE.sub(lambda _m: canonical, html, count=1)
    else:
        anchor = re.search(r'<meta name="description" content="[^"]*">', html)
        if not anchor:
            raise ConfigError(f"{name}: không tìm thấy thẻ meta description để đặt canonical ngay sau.")
        html = html[:anchor.end()] + "\n  " + canonical + html[anchor.end():]
    html = OG_URL_RE.sub(lambda _m: f'<meta property="og:url" content="{url}">', html)
    return html


def write_config_block(html, cfg):
    block = json_for_script(cfg)
    if CONFIG_RE.search(html):
        return CONFIG_RE.sub(lambda m: m.group(1) + block + m.group(3), html, count=1)
    canonical = CANONICAL_RE.search(html)
    if not canonical:
        raise ConfigError("Chưa có canonical để đặt khối cấu hình ngay sau.")
    tag = f'\n  <script type="application/json" id="w17-site-config">{block}</script>'
    return html[:canonical.end()] + tag + html[canonical.end():]


def merge_changes(cfg, changes):
    """Trả (cấu hình mới, danh sách (trường, cũ, mới)) sau khi kiểm từng giá trị người dùng gửi."""
    if not isinstance(changes, dict):
        raise ConfigError("Dữ liệu cài đặt phải là object.")
    new_cfg = json.loads(json.dumps(cfg))
    diffs = []
    unknown = [k for k in changes if k not in FIELDS]
    if unknown:
        raise ConfigError("Trường không hỗ trợ: " + ", ".join(sorted(unknown)))
    for dotted, raw in changes.items():
        value = validate_value(dotted, raw)
        old = get(cfg, dotted)
        if value != old:
            _set(new_cfg, dotted, value)
            diffs.append((dotted, old, value))
    return new_cfg, diffs


def render_pages(pages, cfg, diffs):
    """pages: {tên file: html}. Trả ({tên file: html mới}, {trường: số chỗ đã thay ở mỗi file})."""
    out, counts = {}, {}
    for name, html in pages.items():
        for dotted, old, new in diffs:
            spec = FIELDS[dotted]
            if "before" not in spec:
                continue  # địa chỉ web chỉ nằm ở canonical/og:url, đặt lại bên dưới
            html, n = _replace_bounded(html, old, new, spec)
            counts.setdefault(dotted, {})[name] = n
        html = apply_site_tags(html, name, cfg)
        html = write_config_block(html, cfg)
        out[name] = html
    return out, counts


def check(root=ROOT):
    """Danh sách lỗi (rỗng = OK)."""
    problems, configs, scripts = [], {}, {}
    for name in FINALS:
        try:
            html = read(Path(root) / name)
            cfg = parse_config(html)
        except (OSError, ConfigError) as err:
            problems.append(f"{name}: {err}")
            continue
        if cfg is None:
            problems.append(f"{name}: thiếu khối w17-site-config")
            continue
        configs[name] = cfg
        url = page_urls(cfg)[name]
        tags = CANONICAL_RE.findall(html)
        if tags != [f'<link rel="canonical" href="{url}">']:
            problems.append(f"{name}: canonical phải là đúng một thẻ trỏ tới {url}, thực tế {tags}")
        for og in OG_URL_RE.findall(html):
            if og != f'<meta property="og:url" content="{url}">':
                problems.append(f"{name}: og:url sai ({og})")
        for dotted, spec in FIELDS.items():
            if "before" in spec and get(cfg, dotted) not in html.replace(CONFIG_RE.search(html).group(0), ""):
                problems.append(f"{name}: giá trị {dotted} không xuất hiện ở đâu ngoài khối cấu hình")
        found = SETTINGS_SCRIPT_RE.findall(html)
        if len(found) != 1:
            problems.append(f"{name}: cần đúng một <script id=\"w17-settings-script\">, thực tế {len(found)}")
        else:
            scripts[name] = found[0]
    if len(configs) == 2 and configs[PORTFOLIO] != configs[CV]:
        problems.append("Khối w17-site-config của Portfolio và CV khác nhau")
    if len(scripts) == 2 and scripts[PORTFOLIO] != scripts[CV]:
        problems.append("Mã w17-settings-script của Portfolio và CV khác nhau")
    return problems


def main(argv):
    if "--show" in argv:
        print(json.dumps(parse_config(read(ROOT / PORTFOLIO)), ensure_ascii=False, indent=2))
        return 0
    problems = check()
    for p in problems:
        print("LỖI    " + p)
    if not problems:
        print("OK     w17-site-config hợp lệ, giống nhau ở hai trang; canonical/og:url đúng")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
