"""Tiny builder for Elementor (v3 container) JSON.

Every template in this repo is generated from Python so the output is always
valid JSON, IDs are unique and every widget follows the same styling rules.
"""
import hashlib
import json
from urllib.parse import quote

_counter = [0]
_used = set()


def eid():
    """Deterministic, unique 7-char hex id (same format Elementor uses)."""
    while True:
        _counter[0] += 1
        h = hashlib.md5(f"be-organic-{_counter[0]}".encode()).hexdigest()[:7]
        if h not in _used and not h.isdigit():
            _used.add(h)
            return h


def reset_ids(namespace):
    _counter[0] = int(hashlib.md5(namespace.encode()).hexdigest()[:6], 16)


# ---------------------------------------------------------------- values
def px(v, unit="px"):
    return {"unit": unit, "size": v, "sizes": []}


def em(v):
    return px(v, "em")


def dims(t, r=None, b=None, l=None, unit="px"):
    r = t if r is None else r
    b = t if b is None else b
    l = r if l is None else l
    vals = [str(t), str(r), str(b), str(l)]
    return {"unit": unit, "top": vals[0], "right": vals[1], "bottom": vals[2],
            "left": vals[3], "isLinked": len(set(vals)) == 1}


def gaps(row, col=None, unit="px"):
    col = row if col is None else col
    return {"column": str(col), "row": str(row), "isLinked": row == col, "unit": unit}


def gcol(cid):
    return f"globals/colors?id={cid}"


def gtyp(tid):
    return f"globals/typography?id={tid}"


def fa(name, lib="fa-solid"):
    return {"value": name, "library": lib}


def tag(name, settings=None):
    """Dynamic tag shortcode exactly as Elementor stores it."""
    s = quote(json.dumps(settings or {}, separators=(",", ":")), safe="")
    return f'[elementor-tag id="{eid()}" name="{name}" settings="{s}"]'


# ---------------------------------------------------------------- settings helpers
def merge(*dicts):
    out = {}
    glob = {}
    dyn = {}
    for d in dicts:
        if not d:
            continue
        for k, v in d.items():
            if k == "__globals__":
                glob.update(v)
            elif k == "__dynamic__":
                dyn.update(v)
            else:
                out[k] = v
    if glob:
        out["__globals__"] = glob
    if dyn:
        out["__dynamic__"] = dyn
    return out


def resp(key, desktop=None, tablet=None, mobile=None):
    out = {}
    if desktop is not None:
        out[key] = desktop
    if tablet is not None:
        out[key + "_tablet"] = tablet
    if mobile is not None:
        out[key + "_mobile"] = mobile
    return out


def typo(prefix, tid):
    """Bind a typography group to a global typography preset."""
    return {"__globals__": {f"{prefix}_typography": gtyp(tid)}}


def color(key, cid):
    return {"__globals__": {key: gcol(cid)}}


def bg_color(cid, prefix="background"):
    return {f"{prefix}_background": "classic", "__globals__": {f"{prefix}_color": gcol(cid)}}


def border(width=1, cid="boborder", style="solid", prefix="border", radius=None, radius_key="border_radius"):
    out = {f"{prefix}_border": style, f"{prefix}_width": dims(width),
           "__globals__": {f"{prefix}_color": gcol(cid)}}
    if radius is not None:
        out[radius_key] = dims(radius)
    return out


def css_class(name):
    return {"_css_classes": name}


def hide(desktop=False, tablet=False, mobile=False):
    out = {}
    if desktop:
        out["hide_desktop"] = "hidden-desktop"
    if tablet:
        out["hide_tablet"] = "hidden-tablet"
    if mobile:
        out["hide_mobile"] = "hidden-mobile"
    return out


# ---------------------------------------------------------------- elements
def widget(wtype, *settings):
    return {"id": eid(), "elType": "widget", "isInner": False,
            "settings": merge(*settings), "elements": [], "widgetType": wtype}


def container(children, *settings, inner=False):
    s = merge(*settings)
    if "_css_classes" in s:  # containers use 'css_classes' (widgets use '_css_classes')
        s["css_classes"] = (s.pop("_css_classes") + " " + s.get("css_classes", "")).strip()
    return {"id": eid(), "elType": "container", "isInner": inner, "settings": s, "elements": children}


def flex(children, direction="column", gap=None, *settings, inner=True, align=None, justify=None,
         boxed=False, wrap=None):
    s = {"container_type": "flex", "content_width": "boxed" if boxed else "full",
         "flex_direction": direction}
    if gap is not None:
        s["flex_gap"] = gaps(gap) if not isinstance(gap, dict) else gap
    if align:
        s["flex_align_items"] = align
    if justify:
        s["flex_justify_content"] = justify
    if wrap:
        s["flex_wrap"] = wrap
    s.setdefault("padding", dims(0))
    return container(children, s, *settings, inner=inner)


def grid(children, cols, gap_row, gap_col=None, *settings, inner=True, rows="auto", boxed=False,
         cols_tablet=None, cols_mobile="1fr", align=None, justify_items=None):
    """Grid container. cols are CSS track lists ('1fr 1fr', '2fr 1fr' ...)."""
    s = {"container_type": "grid", "content_width": "boxed" if boxed else "full",
         "grid_columns_grid": {"unit": "custom", "size": cols, "sizes": []},
         "grid_rows_grid": {"unit": "custom", "size": rows, "sizes": []},
         "grid_gaps": gaps(gap_row, gap_col),
         "grid_auto_flow": "row",
         "grid_outline": "",
         "padding": dims(0)}
    if cols_tablet is not None:
        s["grid_columns_grid_tablet"] = {"unit": "custom", "size": cols_tablet, "sizes": []}
    if cols_mobile is not None:
        s["grid_columns_grid_mobile"] = {"unit": "custom", "size": cols_mobile, "sizes": []}
        s["grid_rows_grid_mobile"] = {"unit": "custom", "size": "auto", "sizes": []}
    if align:
        s["grid_align_items"] = align
    if justify_items:
        s["grid_justify_items"] = justify_items
    return container(children, s, *settings, inner=inner)


def section(children, *settings, full=False, direction="column", gap=0, pad=(80, 24, 80, 24),
            pad_tablet=None, pad_mobile=None):
    """Top-level section: boxed to the kit width (1300px), padded for small screens."""
    s = {"container_type": "flex", "content_width": "full" if full else "boxed",
         "flex_direction": direction, "flex_gap": gaps(gap),
         "padding": dims(*pad)}
    if pad_tablet:
        s["padding_tablet"] = dims(*pad_tablet)
    if pad_mobile:
        s["padding_mobile"] = dims(*pad_mobile)
    return container(children, s, *settings, inner=False)


# ---------------------------------------------------------------- common widgets
def heading(text, tag_="h2", typ="secondary", col="boink", align=None, link=None, *extra, dynamic=None):
    s = {"title": text, "header_size": tag_}
    if align:
        s.update(align if isinstance(align, dict) else {"align": align})
    if link:
        s["link"] = {"url": link, "is_external": "", "nofollow": ""}
    d = {"__dynamic__": {"title": dynamic}} if dynamic else None
    return widget("heading", s, typo("typography", typ), color("title_color", col), d, *extra)


def text(html, typ="text", col="text", align=None, *extra):
    s = {"editor": html}
    if align:
        s.update(align if isinstance(align, dict) else {"align": align})
    return widget("text-editor", s, typo("typography", typ), color("text_color", col),
                  {"paragraph_spacing": px(0)}, *extra)


def image_box(title, desc, title_tag="h2", title_typ="secondary", desc_typ="text",
              title_col="boink", desc_col="text", align="left", title_gap=14, *extra,
              align_tablet=None, align_mobile=None):
    """Image Box with the image removed = clean heading + description pair."""
    s = {"image": {"url": "", "id": ""}, "title_text": title, "description_text": desc,
         "title_size": title_tag, "position": "top", "text_align": align,
         "title_bottom_space": px(title_gap), "image_space": px(0)}
    if align_tablet:
        s["text_align_tablet"] = align_tablet
    if align_mobile:
        s["text_align_mobile"] = align_mobile
    return widget("image-box", s, typo("title_typography", title_typ),
                  typo("description_typography", desc_typ),
                  color("title_color", title_col), color("description_color", desc_col), *extra)


def button(label, url="#", style="dark", icon=True, align=None, full=False, *extra, icon_before=False,
           dynamic_link=None, pad=(17, 30, 17, 30)):
    """Brand buttons. style: dark | gold | text-gold | text-dark."""
    s = {"text": label, "link": {"url": url, "is_external": "", "nofollow": ""},
         "size": "md", "border_radius": dims(4), "text_padding": dims(*pad)}
    if icon:
        s["selected_icon"] = fa("fas fa-arrow-left" if icon_before else "fas fa-arrow-right")
        s["icon_align"] = "row" if icon_before else "row-reverse"
        s["icon_indent"] = px(10)
    if align:
        s.update(align if isinstance(align, dict) else {"align": align})
    if full:
        s["align"] = "justify"
    g = {}
    if style == "dark":
        s["background_background"] = "classic"
        g = {"background_color": gcol("primary"), "button_text_color": gcol("bowhite"),
             "button_background_hover_color": gcol("bodeep"), "hover_color": gcol("bowhite")}
        s["button_background_hover_background"] = "classic"
    elif style == "gold":
        s["background_background"] = "classic"
        s["button_background_hover_background"] = "classic"
        g = {"background_color": gcol("secondary"), "button_text_color": gcol("bowhite"),
             "button_background_hover_color": gcol("primary"), "hover_color": gcol("bowhite")}
    elif style in ("text-gold", "text-dark"):
        s["background_background"] = "classic"
        s["background_color"] = "#02010100"
        s["button_background_hover_background"] = "classic"
        s["button_background_hover_color"] = "#02010100"
        s["text_padding"] = dims(0)
        cid = "bogold" if style == "text-gold" else "boink"
        g = {"button_text_color": gcol(cid), "hover_color": gcol("primary")}
    d = {"__dynamic__": {"link": dynamic_link}} if dynamic_link else None
    return widget("button", s, {"__globals__": g}, typo("typography", "accent"), d, *extra)


def image(url, alt="", height=None, radius=0, *extra, height_tablet=None, height_mobile=None,
          img_id=""):
    s = {"image": {"url": url, "id": img_id, "size": "", "alt": alt, "source": "library"},
         "image_size": "full", "width": px(100, "%"), "align": "center"}
    if height:
        s.update({"height": px(height), "object-fit": "cover", "object-position": "center center"})
    if height_tablet:
        s["height_tablet"] = px(height_tablet)
    if height_mobile:
        s["height_mobile"] = px(height_mobile)
    if radius:
        s["image_border_radius"] = dims(radius)
    return widget("image", s, *extra)


def html(code, *extra):
    return widget("html", {"html": code}, *extra)


def custom_css(css):
    return {"custom_css": css.strip() + "\n"}
