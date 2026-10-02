"""Be Organic design system -> Elementor Site Settings (global colors + fonts).

Change a value here (or later in Elementor > Site Settings) and every
template that references it updates automatically.
"""
from elem import px, em, dims

HEADING_FONT = "Newsreader"
BODY_FONT = "Jost"

SYSTEM_COLORS = [
    ("primary", "Forest Green (Primary)", "#1F3D2B"),
    ("secondary", "Golden Harvest (Secondary)", "#B38746"),
    ("text", "Body Text", "#4A4841"),
    ("accent", "Sage Mist (Accent)", "#DCE3D3"),
]

CUSTOM_COLORS = [
    ("bocream", "Cream Canvas (Page BG)", "#F8F4EE"),
    ("bopaper", "Paper Card", "#FCFAF6"),
    ("boink", "Heading Ink", "#16291E"),
    ("bomuted", "Muted Text", "#6B6961"),
    ("bogold", "Gold Text / Links", "#9A7640"),
    ("boborder", "Soft Border", "#E2DED6"),
    ("bodeep", "Deep Green (Hover)", "#142B1D"),
    ("bowhite", "Pure White", "#FFFFFF"),
]


def _t(family, weight, size, size_t=None, size_m=None, lh=None, ls=None, transform=None):
    d = {"typography_typography": "custom", "typography_font_family": family,
         "typography_font_weight": str(weight), "typography_font_size": px(size)}
    if size_t:
        d["typography_font_size_tablet"] = px(size_t)
    if size_m:
        d["typography_font_size_mobile"] = px(size_m)
    if lh:
        d["typography_line_height"] = em(lh)
    if ls is not None:
        d["typography_letter_spacing"] = px(ls)
    if transform:
        d["typography_text_transform"] = transform
    return d


SYSTEM_TYPOGRAPHY = [
    ("primary", "Display H1", _t(HEADING_FONT, 500, 64, 50, 40, 1.08, -1)),
    ("secondary", "Section H2", _t(HEADING_FONT, 500, 44, 36, 31, 1.15, -0.5)),
    ("text", "Body", _t(BODY_FONT, 400, 17, 16, 16, 1.65)),
    ("accent", "Button", _t(BODY_FONT, 500, 16, 16, 15, 1.2, 0.2)),
]

CUSTOM_TYPOGRAPHY = [
    ("boh3", "Box Heading H3", _t(HEADING_FONT, 500, 34, 30, 27, 1.2, -0.3)),
    ("boh4", "Card Title H4", _t(HEADING_FONT, 500, 25, 23, 22, 1.25, -0.2)),
    ("boh5", "Small Heading H5", _t(HEADING_FONT, 500, 20, 19, 18, 1.35)),
    ("bolead", "Lead Paragraph", _t(BODY_FONT, 400, 19, 18, 17, 1.6)),
    ("bosmall", "Small Text", _t(BODY_FONT, 400, 15, 15, 15, 1.6)),
    ("boeyebrow", "Eyebrow", _t(BODY_FONT, 500, 13, 13, 12, 1.4, 2.6, "uppercase")),
    ("bonav", "Menu", _t(BODY_FONT, 400, 15, 15, 16, 1.4)),
    ("bologo", "Logo", _t(HEADING_FONT, 500, 30, 27, 24, 1, 0.5, "uppercase")),
]

COLOR_HEX = {cid: hexv for cid, _, hexv in SYSTEM_COLORS + CUSTOM_COLORS}


def kit_settings():
    """Settings payload for the Elementor kit (Site Settings)."""
    s = {
        "system_colors": [{"_id": i, "title": t, "color": c} for i, t, c in SYSTEM_COLORS],
        "custom_colors": [{"_id": i, "title": t, "color": c} for i, t, c in CUSTOM_COLORS],
        "system_typography": [dict({"_id": i, "title": t}, **d) for i, t, d in SYSTEM_TYPOGRAPHY],
        "custom_typography": [dict({"_id": i, "title": t}, **d) for i, t, d in CUSTOM_TYPOGRAPHY],
        "default_generic_fonts": "Sans-serif",
        # Layout
        "container_width": px(1300),
        "container_width_tablet": px(1024),
        "container_width_mobile": px(767),
        "container_padding": dims(0),
        "space_between_widgets": {"column": "20", "row": "20", "isLinked": True, "unit": "px"},
        "page_title_selector": "h1.entry-title",
        "viewport_md": 768,
        "viewport_lg": 1025,
        # Body
        "body_background_background": "classic",
        "body_background_color": COLOR_HEX["bocream"],
        "body_color": COLOR_HEX["text"],
        "body_typography_typography": "custom",
        "link_normal_color": COLOR_HEX["bogold"],
        "link_hover_color": COLOR_HEX["primary"],
        "__globals__": {
            "body_background_color": "globals/colors?id=bocream",
            "body_color": "globals/colors?id=text",
            "body_typography_typography": "globals/typography?id=text",
            "link_normal_color": "globals/colors?id=bogold",
            "link_hover_color": "globals/colors?id=primary",
            "h1_color": "globals/colors?id=boink",
            "h1_typography_typography": "globals/typography?id=primary",
            "h2_color": "globals/colors?id=boink",
            "h2_typography_typography": "globals/typography?id=secondary",
            "h3_color": "globals/colors?id=boink",
            "h3_typography_typography": "globals/typography?id=boh3",
            "h4_color": "globals/colors?id=boink",
            "h4_typography_typography": "globals/typography?id=boh4",
            "h5_color": "globals/colors?id=boink",
            "h5_typography_typography": "globals/typography?id=boh5",
            "h6_color": "globals/colors?id=boink",
            "h6_typography_typography": "globals/typography?id=boeyebrow",
            "button_typography_typography": "globals/typography?id=accent",
            "button_text_color": "globals/colors?id=bowhite",
            "button_background_color": "globals/colors?id=primary",
            "button_hover_text_color": "globals/colors?id=bowhite",
            "button_hover_background_color": "globals/colors?id=bodeep",
            "form_field_text_color": "globals/colors?id=boink",
            "form_field_background_color": "globals/colors?id=bowhite",
            "form_field_border_color": "globals/colors?id=boborder",
            "form_label_color": "globals/colors?id=boink",
        },
        "h1_typography_typography": "custom", "h2_typography_typography": "custom",
        "h3_typography_typography": "custom", "h4_typography_typography": "custom",
        "h5_typography_typography": "custom", "h6_typography_typography": "custom",
        "button_typography_typography": "custom",
        "button_background_background": "classic",
        "button_hover_background_background": "classic",
        "button_border_radius": dims(4),
        "button_padding": dims(16, 30, 16, 30),
        "form_field_border_border": "solid",
        "form_field_border_width": dims(1),
        "form_field_border_radius": dims(4),
        "form_field_padding": dims(13, 16, 13, 16),
        "site_name": "Be Organic",
        "site_description": "Simple ingredients. Everyday inspiration.",
    }
    return s


def fallback_css():
    """:root fallbacks so the design still renders before the kit is imported.

    Elementor defines the real variables on body.elementor-kit-N, which is
    closer to the content than :root, so the Site Settings always win.
    """
    lines = []
    for cid, _, hexv in SYSTEM_COLORS + CUSTOM_COLORS:
        lines.append(f"--e-global-color-{cid}:{hexv};")
    for tid, _, d in SYSTEM_TYPOGRAPHY + CUSTOM_TYPOGRAPHY:
        lines.append(f'--e-global-typography-{tid}-font-family:"{d["typography_font_family"]}";')
        lines.append(f'--e-global-typography-{tid}-font-weight:{d["typography_font_weight"]};')
        lines.append(f'--e-global-typography-{tid}-font-size:{d["typography_font_size"]["size"]}px;')
        if "typography_line_height" in d:
            lines.append(f'--e-global-typography-{tid}-line-height:{d["typography_line_height"]["size"]}em;')
        if "typography_letter_spacing" in d:
            lines.append(f'--e-global-typography-{tid}-letter-spacing:{d["typography_letter_spacing"]["size"]}px;')
        if "typography_text_transform" in d:
            lines.append(f'--e-global-typography-{tid}-text-transform:{d["typography_text_transform"]};')
    return ":root{" + "".join(lines) + "}"
