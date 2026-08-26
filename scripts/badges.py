#!/usr/bin/env python3
"""Draw the badges that sit at the top of the profile.

Shields.io and the language pills were three different systems stacked on top
of each other: different heights, different corner radii, different typefaces,
and a label segment dark enough to read as a hole in the badge. These are drawn
here instead, so the first block a visitor sees is one typeface at one size.
"""

import io
import os

MONO = "'JetBrains Mono','SFMono-Regular',Consolas,'Liberation Mono',monospace"

ACCENT = "#1f6feb"
ACCENT_EDGE = "#4c9aff"
ACCENT_TEXT = "#58a6ff"
SURFACE = "#10161f"
EDGE = "#2b3949"
MUTED = "#8b9cb0"
TEXT = "#c9d6e4"

PILL_H = 34
FLAG_W = 22
FLAG_H = 15


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
        '  <rect x="0.5" y="0.5" width="%s" height="%s" rx="9" fill="%s" stroke="%s"/>\n'
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
        '<rect x="0" y="0" width="%s" height="%s" rx="2"/></clipPath></defs>\n'
        '  <rect x="0.5" y="0.5" width="%s" height="%s" rx="9" fill="%s" stroke="%s"/>\n'
        '  <g transform="translate(13 %s)">'
        '<g clip-path="url(#flagclip)">%s</g>'
        '<rect x="0.25" y="0.25" width="%s" height="%s" rx="2" fill="none"'
        ' stroke="#0d1117" stroke-opacity="0.4"/></g>\n'
        '  <text x="%s" y="22.3" font-family="%s" font-size="%s" font-weight="600"'
        ' fill="%s" letter-spacing="%s">%s</text>'
        % (FLAG_W, FLAG_H, n(width - 1), PILL_H - 1, bg, edge,
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

    parts = ['  <rect x="0.5" y="0.5" width="%s" height="%s" rx="10" fill="%s" stroke="%s"/>'
             % (n(total - 1), n(height - 1), SURFACE, EDGE)]
    x = 0.0
    for i, (value, label) in enumerate(cells):
        if i:
            parts.append('  <line x1="%s" y1="10" x2="%s" y2="28" stroke="%s" stroke-width="1"/>'
                         % (n(x), n(x), EDGE))
        parts.append('  <text x="%s" y="24.6" font-family="%s" font-size="%s" font-weight="700"'
                     ' fill="%s" letter-spacing="%s">%s</text>'
                     % (n(x + pad), MONO, vsize, ACCENT_TEXT, vtrack, value))
        parts.append('  <text x="%s" y="24.2" font-family="%s" font-size="%s" font-weight="500"'
                     ' fill="%s" letter-spacing="%s">%s</text>'
                     % (n(x + pad + text_width(value, vsize, vtrack) + gap),
                        MONO, lsize, MUTED, ltrack, label))
        x += widths[i]
    return document(total, height, "\n".join(parts))


def write_all(root, en, it, merged_count, project_count, plugin_version):
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
            (plugin_version, strings["badge_plugin"]),
        ])
    for name, content in files.items():
        path = os.path.join(root, "assets", name)
        io.open(path, "w", encoding="utf-8", newline="\n").write(content)
    return sorted(files)
