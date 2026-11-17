#!/usr/bin/env python3
"""Draw the badges that sit at the top of the profile.

Shields.io and the language pills were three different systems stacked on top
of each other: different heights, different corner radii, different typefaces,
and a label segment dark enough to read as a hole in the badge. These are drawn
here instead, so the first block a visitor sees is one typeface at one size.

Every asset carries inline CSS keyframes and a prefers-reduced-motion query
that disables them; no JavaScript, no external fonts.
"""

import io
import math
import os

MONO = "'JetBrains Mono','SFMono-Regular',Consolas,'Liberation Mono',monospace"

ACCENT = "#1f6feb"
ACCENT_EDGE = "#4c9aff"
ACCENT_TEXT = "#58a6ff"
SURFACE = "#10161f"
EDGE = "#2b3949"
MUTED = "#8b9cb0"
TEXT = "#c9d6e4"

BG = "#0d1117"
LIGHT = "#e6edf3"
GRAY = "#8b949e"
STATUS_INK = {"released": "#1f6feb", "pre-alpha": "#d29922", "live": "#238636"}

PILL_H = 34
FLAG_W = 22
FLAG_H = 15
CARD_W, CARD_H = 580.0, 150.0

REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
FADEUP = ("@keyframes fadeup{from{opacity:0;transform:translateY(8px)}"
          "to{opacity:1;transform:translateY(0)}}")
EDGE_PULSE = (
    ".edge{animation:edgepulse 3.4s ease-in-out infinite}"
    "@keyframes edgepulse{0%,100%{stroke-opacity:.5;"
    "filter:drop-shadow(0 0 0 rgba(88,166,255,0))}"
    "50%{stroke-opacity:1;filter:drop-shadow(0 0 3px rgba(88,166,255,.5))}}"
)
BREATHE = (
    ".breathe{transform-box:fill-box;transform-origin:center;"
    "animation:breathe 3.4s ease-in-out infinite}"
    "@keyframes breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.03)}}"
)


def n(value):
    return ("%.2f" % value).rstrip("0").rstrip(".")


def advance(size, tracking):
    """Horizontal advance of one monospace glyph at this size."""
    return size * 0.6 + tracking


def text_width(s, size, tracking):
    return max(0.0, len(s) * advance(size, tracking) - tracking)


def document(width, height, body, label=""):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" width="%s" height="%s"'
        ' role="img" aria-label="%s">\n%s\n</svg>\n'
        % (n(width), n(height), n(width), n(height), label, body)
    )


def style(css):
    return '  <defs><style>%s%s</style></defs>\n' % (css, REDUCED)


def icon_linkedin(ink):
    return (
        '<rect width="16" height="16" rx="3.2" fill="%s"/>'
        '<text x="8" y="11.9" text-anchor="middle" font-family="%s" font-size="9.5"'
        ' font-weight="700" fill="%s">in</text>' % (ink, MONO, ACCENT)
    )


def icon_email(ink):
    return (
        '<rect x="0.9" y="2.6" width="14.2" height="10.8" rx="2.2" fill="none"'
        ' stroke="%s" stroke-width="1.5"/>'
        '<path d="M1.9 4.6 L8 9.2 L14.1 4.6" fill="none" stroke="%s" stroke-width="1.5"'
        ' stroke-linecap="round" stroke-linejoin="round"/>' % (ink, ink)
    )


def icon_pin(ink):
    return (
        '<path d="M8 1 C5.1 1 2.7 3.4 2.7 6.3 c0 3.8 5.3 8.7 5.3 8.7 s5.3 -4.9 5.3 -8.7'
        ' C13.3 3.4 10.9 1 8 1 z" fill="none" stroke="%s" stroke-width="1.5"'
        ' stroke-linejoin="round"/>'
        '<circle cx="8" cy="6.2" r="1.9" fill="%s"/>' % (ink, ink)
    )


ICONS = {"linkedin": icon_linkedin, "email": icon_email, "pin": icon_pin}

FLAG_UK = (
    '<rect width="22" height="15" fill="#012169"/>'
    '<path d="M0 0 L22 15 M22 0 L0 15" stroke="#ffffff" stroke-width="3"/>'
    '<path d="M0 0 L22 15 M22 0 L0 15" stroke="#C8102E" stroke-width="1.5"/>'
    '<path d="M11 0 V15 M0 7.5 H22" stroke="#ffffff" stroke-width="4.6"/>'
    '<path d="M11 0 V15 M0 7.5 H22" stroke="#C8102E" stroke-width="2.6"/>'
)

FLAG_IT = (
    '<rect width="7.34" height="15" fill="#008C45"/>'
    '<rect x="7.34" y="0" width="7.33" height="15" fill="#F4F5F0"/>'
    '<rect x="14.67" y="0" width="7.33" height="15" fill="#CD212A"/>'
)

LABEL_SIZE = 11.5
LABEL_TRACK = 1.3


def pill(label, icon, filled=False):
    width = 13 + 16 + 9 + text_width(label, LABEL_SIZE, LABEL_TRACK) + 15
    if filled:
        bg, edge, fg, ink = ACCENT, ACCENT_EDGE, "#ffffff", "#ffffff"
    else:
        bg, edge, fg, ink = SURFACE, EDGE, TEXT, ACCENT_TEXT
    body = (
        style(EDGE_PULSE) +
        '  <rect class="edge" x="0.5" y="0.5" width="%s" height="%s" rx="9" fill="%s" stroke="%s"/>\n'
        '  <g transform="translate(13 9)">%s</g>\n'
        '  <text x="38" y="22.3" font-family="%s" font-size="%s" font-weight="600"'
        ' fill="%s" letter-spacing="%s">%s</text>'
        % (n(width - 1), PILL_H - 1, bg, edge, ICONS[icon](ink),
           MONO, LABEL_SIZE, fg, LABEL_TRACK, label)
    )
    return document(width, PILL_H, body, label)


def language_pill(flag, label, active):
    width = 13 + FLAG_W + 9 + text_width(label, LABEL_SIZE, LABEL_TRACK) + 15
    if active:
        bg, edge, fg = ACCENT, ACCENT_EDGE, "#ffffff"
    else:
        bg, edge, fg = SURFACE, EDGE, MUTED
    body = (
        '  <defs><clipPath id="flagclip">'
        '<rect x="0" y="0" width="%s" height="%s" rx="2"/></clipPath>'
        '<style>%s%s%s</style></defs>\n'
        '  <g%s>\n'
        '  <rect class="edge" x="0.5" y="0.5" width="%s" height="%s" rx="9" fill="%s" stroke="%s"/>\n'
        '  <g transform="translate(13 %s)">'
        '<g clip-path="url(#flagclip)">%s</g>'
        '<rect x="0.25" y="0.25" width="%s" height="%s" rx="2" fill="none"'
        ' stroke="#0d1117" stroke-opacity="0.4"/></g>\n'
        '  <text x="%s" y="22.3" font-family="%s" font-size="%s" font-weight="600"'
        ' fill="%s" letter-spacing="%s">%s</text>\n'
        '  </g>'
        % (FLAG_W, FLAG_H, EDGE_PULSE, BREATHE if active else "", REDUCED,
           ' class="breathe"' if active else "",
           n(width - 1), PILL_H - 1, bg, edge,
           n((PILL_H - FLAG_H) / 2.0), flag,
           n(FLAG_W - 0.5), n(FLAG_H - 0.5),
           n(13 + FLAG_W + 9), MONO, LABEL_SIZE, fg, LABEL_TRACK, label)
    )
    return document(width, PILL_H, body, label)


def stats_bar(cells):
    """One bar for the counters. cells is a list of (value, label)."""
    vsize, vtrack = 15.0, 0.5
    lsize, ltrack = 10.5, 1.4
    pad, gap, height = 22.0, 11.0, 38.0

    widths = [pad + text_width(v, vsize, vtrack) + gap + text_width(l, lsize, ltrack) + pad
              for v, l in cells]
    total = sum(widths)

    css = (
        ".cell{animation:fadeup .6s cubic-bezier(.22,.61,.36,1) both}"
        + FADEUP +
        "".join(".c%d{animation-delay:%ss}" % (i + 1, n(0.05 + i * 0.15))
                for i in range(len(cells))) +
        ".num{animation:glow 3s ease-in-out infinite}"
        "@keyframes glow{0%,100%{filter:drop-shadow(0 0 0 rgba(88,166,255,0))}"
        "50%{filter:drop-shadow(0 0 5px rgba(88,166,255,.6))}}"
        ".sweep{animation:sweep 4.5s linear infinite}"
        + "@keyframes sweep{from{transform:translateX(-160px)}to{transform:translateX(%spx)}}"
        % n(total)
    )
    parts = [
        '  <defs><style>%s%s</style>'
        '<linearGradient id="sweepgrad" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0" stop-color="#58a6ff" stop-opacity="0"/>'
        '<stop offset="0.5" stop-color="#58a6ff" stop-opacity="0.14"/>'
        '<stop offset="1" stop-color="#58a6ff" stop-opacity="0"/></linearGradient>'
        '<clipPath id="barclip"><rect x="0.5" y="0.5" width="%s" height="%s" rx="10"/></clipPath></defs>'
        % (css, REDUCED, n(total - 1), n(height - 1)),
        '  <rect x="0.5" y="0.5" width="%s" height="%s" rx="10" fill="%s" stroke="%s"/>'
        % (n(total - 1), n(height - 1), SURFACE, EDGE),
        '  <g clip-path="url(#barclip)">'
        '<rect class="sweep" x="0" y="1" width="140" height="%s" fill="url(#sweepgrad)"/></g>'
        % n(height - 2),
    ]
    x = 0.0
    for i, (value, label) in enumerate(cells):
        cell = []
        if i:
            cell.append('  <line x1="%s" y1="10" x2="%s" y2="28" stroke="%s" stroke-width="1"/>'
                        % (n(x), n(x), EDGE))
        cell.append('  <text class="num" x="%s" y="24.6" font-family="%s" font-size="%s" font-weight="700"'
                    ' fill="%s" letter-spacing="%s">%s</text>'
                    % (n(x + pad), MONO, vsize, ACCENT_TEXT, vtrack, value))
        cell.append('  <text x="%s" y="24.2" font-family="%s" font-size="%s" font-weight="500"'
                    ' fill="%s" letter-spacing="%s">%s</text>'
                    % (n(x + pad + text_width(value, vsize, vtrack) + gap),
                       MONO, lsize, MUTED, ltrack, label))
        parts.append('  <g class="cell c%d">\n%s\n  </g>' % (i + 1, "\n".join(cell)))
        x += widths[i]
    return document(total, height, "\n".join(parts))


def wrap(text, size, tracking, max_width, max_lines=2):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if not cur or text_width(trial, size, tracking) <= max_width:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    if len(lines) > max_lines:
        raise ValueError("tagline wraps past %d lines: %s" % (max_lines, text))
    return lines


def card(project, lang):
    """One animated project card: name, tagline, stack chips, status chip."""
    name, label = project["name"], project["label"]
    ink = STATUS_INK[project["status"]]
    tagline = project["tagline"][lang]
    lines = wrap(tagline, 11.5, 0.3, CARD_W - 40)

    chip_w = 22 + text_width(label, 10.5, 0.5) + 12
    chip_x = CARD_W - 20 - chip_w
    rx = 12.0
    perim = 2 * (CARD_W - 1 + CARD_H - 1) - 8 * rx + 2 * math.pi * rx

    css = (
        ".in{animation:fadeup .7s cubic-bezier(.22,.61,.36,1) both}" + FADEUP +
        (".run{stroke-dasharray:90 %s;animation:run 6s linear infinite}"
         "@keyframes run{to{stroke-dashoffset:%s}}" % (n(perim - 90), n(-perim))) +
        ".dot{transform-box:fill-box;transform-origin:center;"
        "animation:dot 2s ease-in-out infinite}"
        "@keyframes dot{0%,100%{opacity:.45;transform:scale(.8)}"
        "50%{opacity:1;transform:scale(1.15)}}"
    )
    parts = [
        style(css),
        '  <g class="in">',
        '  <rect x="0.5" y="0.5" width="%s" height="%s" rx="%s" fill="%s" stroke="%s"/>'
        % (n(CARD_W - 1), n(CARD_H - 1), n(rx), SURFACE, EDGE),
        '  <rect class="run" x="0.5" y="0.5" width="%s" height="%s" rx="%s"'
        ' fill="none" stroke="%s" stroke-width="1.5" stroke-opacity="0.8"/>'
        % (n(CARD_W - 1), n(CARD_H - 1), n(rx), ACCENT_TEXT),
        '  <text x="20" y="36" font-family="%s" font-size="15" font-weight="700"'
        ' fill="%s" letter-spacing="0.5">%s</text>' % (MONO, LIGHT, name),
        '  <rect x="%s" y="18" width="%s" height="22" rx="11" fill="%s"'
        ' stroke="%s" stroke-opacity="0.55"/>'
        % (n(chip_x), n(chip_w), BG, ink),
        '  <circle class="dot" cx="%s" cy="29" r="3" fill="%s"/>' % (n(chip_x + 13), ink),
        '  <text x="%s" y="33" font-family="%s" font-size="10.5" font-weight="600"'
        ' fill="%s" letter-spacing="0.5">%s</text>'
        % (n(chip_x + 22), MONO, ink, label),
    ]
    for i, line in enumerate(lines):
        parts.append('  <text x="20" y="%s" font-family="%s" font-size="11.5"'
                     ' fill="%s" letter-spacing="0.3">%s</text>'
                     % (n(62 + i * 18), MONO, GRAY, line))
    x = 20.0
    for chip in project["stack"]:
        w = text_width(chip, 10.5, 0.5) + 20
        parts.append('  <rect x="%s" y="102" width="%s" height="24" rx="6" fill="%s" stroke="%s"/>'
                     % (n(x), n(w), BG, EDGE))
        parts.append('  <text x="%s" y="118" font-family="%s" font-size="10.5" font-weight="600"'
                     ' fill="%s" letter-spacing="0.5">%s</text>'
                     % (n(x + 10), MONO, ACCENT_TEXT, chip))
        x += w + 8
    parts.append('  </g>')
    return document(CARD_W, CARD_H, "\n".join(parts), "%s: %s" % (name, tagline))


def write_all(root, en, it, projects, merged_count, project_count):
    files = {
        "pill-linkedin.svg": pill("LINKEDIN", "linkedin", filled=True),
        "pill-email.svg": pill("EMAIL", "email"),
        "pill-location-en.svg": pill(en["location"], "pin"),
        "pill-location-it.svg": pill(it["location"], "pin"),
        "lang-en-on.svg": language_pill(FLAG_UK, "ENGLISH", True),
        "lang-en-off.svg": language_pill(FLAG_UK, "ENGLISH", False),
        "lang-it-on.svg": language_pill(FLAG_IT, "ITALIANO", True),
        "lang-it-off.svg": language_pill(FLAG_IT, "ITALIANO", False),
    }
    for code, strings in (("en", en), ("it", it)):
        files["stats-%s.svg" % code] = stats_bar([
            (str(merged_count), strings["badge_merged"]),
            (str(project_count), strings["badge_projects"]),
            (str(len(projects)), strings["badge_own"]),
        ])
        for project in projects:
            files["cards/%s-%s.svg" % (project["name"], code)] = card(project, code)
    for name, content in files.items():
        path = os.path.join(root, "assets", name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        io.open(path, "w", encoding="utf-8", newline="\n").write(content)
    return sorted(files)