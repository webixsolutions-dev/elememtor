"""All Be Organic templates: header, footers, Contact, Did You Know, Single Post,
and the two Loop Item cards. Built with Grid containers (no container-in-container
just for layout), Image Box for heading + description pairs, background image +
gradient overlay on the container itself, Loop Grid for dynamic posts."""
from elem import (eid, reset_ids, px, em, dims, gaps, gcol, gtyp, fa, tag, merge, resp, typo, color,
                  bg_color, border, css_class, hide, widget, container, flex, grid, section, heading,
                  text, image_box, button, image, html, custom_css)
from svgs import leaf_branch, sprig_icon, leaf_outline_art
from css import BASE, FORM, C, F, mask, ARROW, CHEVRON

IMG_BASE = ("https://raw.githubusercontent.com/webixsolutions-dev/elememtor/"
            "refs/heads/claude/elementor-pro-json-file-w1esvf/assets/images/")


def img(name):
    return IMG_BASE + name + ".jpg"


# IDs used inside the kit for the two loop-item templates (Loop Grid -> template_id)
CARD_TEMPLATE_ID = 90101
SPOTLIGHT_TEMPLATE_ID = 90102

SHOP_URL = "/shop/"
DYK_URL = "/did-you-know/"
CONTACT_URL = "/contact/"


def logo_html(light=False, href="/"):
    cls = "bo-logo bo-logo--light" if light else "bo-logo"
    return f'<a class="{cls}" href="{href}" aria-label="Be Organic home">Be Organic {sprig_icon(22)}</a>'


# =====================================================================
# HEADER
# =====================================================================
def header(topbar_cid="primary"):
    reset_ids("header")
    topbar = section([
        heading("Simple ingredients. Everyday inspiration.", "p", "bosmall", "bowhite", "center",
                None, {"typography_font_size": px(14)}),
    ], bg_color(topbar_cid), css_class("bo-topbar"), {"min_height": px(36)},
        {"flex_justify_content": "center", "flex_align_items": "center"},
        full=True, pad=(7, 16, 7, 16))

    nav = widget("nav-menu", {
        "layout": "horizontal", "align_items": "center", "pointer": "underline",
        "animation_line": "fade", "submenu_icon": fa("fas fa-chevron-down"),
        "dropdown": "tablet", "full_width": "", "text_align": "aside", "toggle": "burger",
        "toggle_align": "right",
        "padding_horizontal_menu_item": px(0), "padding_vertical_menu_item": px(8),
        "menu_space_between": px(36), "pointer_width": px(2),
        "toggle_size": px(26), "toggle_border_width": px(0), "toggle_border_radius": px(0),
        "padding_horizontal_dropdown_item": px(24), "padding_vertical_dropdown_item": px(14),
        "dropdown_top_distance": px(18),
    }, typo("menu_typography", "bonav"), typo("dropdown_typography", "bonav"),
        {"__globals__": {
            "color_menu_item": gcol("boink"), "color_menu_item_hover": gcol("primary"),
            "pointer_color_menu_item_hover": gcol("secondary"), "color_menu_item_active": gcol("boink"),
            "pointer_color_menu_item_active": gcol("secondary"), "toggle_color": gcol("boink"),
            "toggle_background_color": gcol("bocream"),
            "color_dropdown_item": gcol("boink"), "background_color_dropdown_item": gcol("bocream"),
            "color_dropdown_item_hover": gcol("bowhite"), "background_color_dropdown_item_hover": gcol("primary"),
            "color_dropdown_item_active": gcol("bowhite"), "background_color_dropdown_item_active": gcol("primary"),
        }},
        css_class("bo-nav"),
        custom_css(f"""
selector .elementor-nav-menu--main .elementor-item{{padding-bottom:8px}}
selector .elementor-nav-menu--main .elementor-item:after{{bottom:-6px;height:2px;background-color:{C('secondary')}}}
selector .elementor-menu-toggle{{background:transparent;padding:4px}}
selector .elementor-nav-menu--dropdown{{box-shadow:0 18px 40px rgba(22,41,30,.12)}}
"""))

    search = widget("search-form", {
        "skin": "full_screen", "toggle_size": px(40), "toggle_align": "center",
    }, {"__globals__": {"toggle_color": gcol("boink"), "toggle_background_color": gcol("bocream")}},
        css_class("bo-search"),
        custom_css(f"""
selector .elementor-search-form__toggle{{--e-search-form-toggle-size:40px;--e-search-form-toggle-color:{C('boink')};--e-search-form-toggle-background-color:transparent;--e-search-form-toggle-icon-size:calc(0.55em)}}
selector .elementor-search-form__toggle i,selector .elementor-search-form__toggle div{{background:transparent!important;color:{C('boink')}}}
selector .elementor-search-form__toggle svg{{fill:{C('boink')};width:21px;height:21px}}
selector .elementor-search-form--full-screen .elementor-search-form__container{{background-color:rgba(22,41,30,.94)}}
"""))

    cart = widget("woocommerce-menu-cart", {
        "icon": "bag-light", "items_indicator": "bubble", "hide_empty_indicator": "yes",
        "show_subtotal": "", "toggle_icon_size": px(24), "toggle_button_padding": dims(4),
        "toggle_button_border_width": dims(0), "alignment": "right",
    }, {"__globals__": {"toggle_button_icon_color": gcol("boink"), "items_indicator_background_color": gcol("secondary"),
                        "items_indicator_text_color": gcol("bowhite"), "toggle_button_background_color": gcol("bocream")}},
        css_class("bo-cart"),
        custom_css(f"""
selector .elementor-menu-cart__toggle .elementor-button{{background:transparent;border:0;padding:4px;color:{C('boink')}}}
selector .elementor-menu-cart__toggle .elementor-button-icon{{font-size:24px;color:{C('boink')}}}
"""))

    icons = flex([search, cart], "row", 18, align="center", justify="flex-end",
                 *[css_class("bo-header-icons")])

    main = section([
        grid([
            html(logo_html(), css_class("bo-header-logo")),
            nav,
            icons,
        ], "1fr auto 1fr", 0, 24, {"grid_align_items": "center"}, cols_tablet="1fr auto auto",
            cols_mobile="1fr auto auto", inner=True),
    ], bg_color("bocream"), css_class("bo-header-main"),
        custom_css(f"""
@media (max-width:1024px){{selector .bo-nav{{order:3}}}}
@media (max-width:767px){{selector .bo-logo{{font-size:22px}}}}
"""),
        pad=(18, 24, 18, 24), pad_mobile=(12, 16, 12, 16))

    return [topbar, main], {"custom_css": BASE + "\n" + _fallback()}


# =====================================================================
# FOOTERS
# =====================================================================
def _social_icons(size=17, align="left"):
    items = [("fab fa-instagram", "https://www.instagram.com/"),
             ("fab fa-pinterest", "https://www.pinterest.com/"),
             ("fab fa-youtube", "https://www.youtube.com/")]
    return widget("social-icons", {
        "social_icon_list": [{"_id": eid(), "social_icon": fa(i, "fa-brands"),
                              "link": {"url": u, "is_external": "on", "nofollow": ""}} for i, u in items],
        "shape": "rounded", "icon_color": "custom", "icon_size": px(size), "icon_padding": em(0.35),
        "icon_spacing": px(12), "align": align, "border_radius": dims(4), "hover_animation": "",
        "align_mobile": "left",
    }, {"__globals__": {"icon_primary_color": gcol("primary"), "icon_secondary_color": gcol("bowhite"),
                        "hover_primary_color": gcol("primary"), "hover_secondary_color": gcol("secondary")}},
        css_class("bo-social"),
        custom_css("selector .elementor-social-icon{background-color:transparent!important}"
                   "selector .elementor-social-icon:hover i{opacity:.85}"))


def _footer_links(items, typ="bosmall", gap=6):
    return widget("icon-list", {
        "view": "traditional",
        "icon_list": [{"_id": eid(), "text": t, "selected_icon": {"value": "", "library": ""},
                       "link": {"url": u, "is_external": "", "nofollow": ""}} for t, u in items],
        "space_between": px(gap), "icon_align": "left",
    }, typo("icon_typography", typ), {"__globals__": {"text_color": gcol("bowhite"), "text_color_hover": gcol("secondary")}},
        css_class("bo-footer-links"))


def _newsletter_form(name, btn_text="Subscribe", btn_cid="primary", field_width="66", btn_width="33",
                     extra_cls="", placeholder="Your email address"):
    return widget("form", {
        "form_name": name,
        "form_fields": [{"_id": eid(), "custom_id": "email", "field_type": "email", "field_label": "Email",
                         "placeholder": placeholder, "required": "true", "width": field_width,
                         "width_mobile": "66"}],
        "input_size": "md", "show_labels": "", "button_text": btn_text, "button_size": "md",
        "button_width": btn_width, "button_width_mobile": "33",
        "submit_actions": ["email"], "email_subject": f"New subscriber - {name}",
        "success_message": "Thank you! You're on the list.",
        "column_gap": px(0), "row_gap": px(0),
        "field_border_width": dims(0), "field_border_radius": dims(4, 0, 0, 4),
        "button_border_radius": dims(0, 4, 4, 0), "button_text_padding": dims(15, 22, 15, 22),
    }, typo("field_typography", "bosmall"), typo("button_typography", "accent"),
        {"__globals__": {"field_text_color": gcol("boink"), "field_background_color": gcol("bowhite"),
                         "button_background_color": gcol(btn_cid), "button_text_color": gcol("bowhite"),
                         "button_background_hover_color": gcol("bodeep"), "button_hover_color": gcol("bowhite")}},
        css_class(("bo-form bo-form--inline " + extra_cls).strip()))


def footer_main():
    """Footer used on Did You Know + Single Post (and site-wide by default)."""
    reset_ids("footer-main")
    brand = flex([
        html(logo_html(light=True)),
        text("<p>Plant-based powders for everyday inspiration.</p>", "bosmall", "bowhite"),
    ], "column", 14)
    explore = flex([
        heading("Explore", "h4", "boh5", "bowhite", None, None, {"typography_font_size": px(18)}),
        _footer_links([("Home", "/"), ("Shop", SHOP_URL), ("About", "/about/"),
                       ("Did You Know", DYK_URL), ("Contact", CONTACT_URL)], gap=4),
    ], "column", 12)
    news = flex([
        heading("Join our newsletter", "h4", "boh5", "bowhite", None, None, {"typography_font_size": px(18)}),
        text("<p>Get simple ideas, new recipes and updates straight to your inbox.</p>", "bosmall", "bowhite",
             None, {"_element_width": "initial", "_element_custom_width": px(340)}),
        _newsletter_form("Footer Newsletter", "", "secondary", "80", "20", "bo-form--icon"),
    ], "column", 12)
    social = flex([_social_icons()], "column", 0, css_class("bo-footer-social"),
                  {"border_border": "solid", "border_width": dims(0, 0, 0, 1),
                   "border_color": "#FFFFFF3D", "padding": dims(4, 0, 4, 36),
                   "padding_mobile": dims(0), "border_width_mobile": dims(0)})
    sec = section([
        grid([brand, explore, news, social], "1.35fr 0.75fr 1.35fr 0.55fr", 40, 48,
             cols_tablet="1fr 1fr", cols_mobile="1fr", inner=True),
    ], bg_color("primary"), css_class("bo-footer"),
        custom_css(f"""
selector .bo-form--icon .elementor-button .elementor-button-text{{display:none}}
selector .bo-form--icon .elementor-button .elementor-button-content-wrapper::after{{margin:0}}
selector .bo-form--icon .elementor-field-type-submit .elementor-button{{padding:0 18px;min-height:46px}}
selector .bo-form--icon .elementor-field-group .elementor-field-textual{{min-height:46px}}
"""),
        pad=(56, 24, 48, 24), pad_mobile=(44, 16, 40, 16))
    return [sec], {"custom_css": BASE + FORM + "\n" + _fallback()}


def footer_contact():
    """Footer variant shown on the Contact mockup."""
    reset_ids("footer-contact")
    brand = flex([
        html(logo_html(light=True)),
        text("<p>Simple ingredients.<br>Everyday inspiration.</p>", "text", "bowhite"),
    ], "column", 14, {"padding": dims(0, 36, 0, 0)})
    links = grid([
        _footer_links([("Home", "/"), ("Shop", SHOP_URL), ("About", "/about/")], gap=8),
        _footer_links([("Did You Know", DYK_URL), ("Contact", CONTACT_URL)], gap=8),
    ], "1fr 1fr", 8, 24, {"border_border": "solid", "border_width": dims(0, 1, 0, 1),
                          "border_color": "#FFFFFF40", "padding": dims(4, 40, 4, 40),
                          "border_width_mobile": dims(0), "padding_mobile": dims(0)},
        cols_mobile="1fr 1fr")
    community = flex([
        heading("Join our community", "h4", "bosmall", "bowhite"),
        _social_icons(18),
    ], "column", 14, {"padding": dims(4, 0, 4, 40), "padding_mobile": dims(0)})
    sec = section([
        grid([brand, links, community], "1.1fr 1.2fr 1fr", 32, 0, {"grid_align_items": "center"},
             cols_tablet="1fr 1fr", cols_mobile="1fr", inner=True),
    ], bg_color("primary"), css_class("bo-footer"), pad=(40, 24, 40, 24), pad_mobile=(40, 16, 40, 16))
    return [sec], {"custom_css": BASE + "\n" + _fallback()}


# =====================================================================
# CONTACT PAGE
# =====================================================================
def contact_page():
    reset_ids("contact")
    leaves_l = html(leaf_branch(260, flip=False, rotate=8, seed=1),
                    {"_position": "absolute", "_offset_orientation_h": "start", "_offset_x": px(-34),
                     "_offset_orientation_v": "start", "_offset_y": px(-6), "_element_width": "initial",
                     "_element_custom_width": px(250), "_z_index": 0, "_offset_x_tablet": px(-70)},
                    hide(mobile=True), css_class("bo-leaves bo-leaves--left"))
    leaves_r = html(leaf_branch(260, flip=True, rotate=14, seed=2),
                    {"_position": "absolute", "_offset_orientation_h": "end", "_offset_x_end": px(-28),
                     "_offset_orientation_v": "start", "_offset_y": px(8), "_element_width": "initial",
                     "_element_custom_width": px(250), "_z_index": 0, "_offset_x_end_tablet": px(-80)},
                    hide(mobile=True), css_class("bo-leaves bo-leaves--right"))

    hero = section([
        leaves_l, leaves_r,
        image_box("Let’s talk goodness.",
                  "Questions about our powders or your order? We’re here to help.",
                  "h1", "primary", "bolead", "boink", "boink", "center", 16,
                  {"_z_index": 1}),
    ], css_class("bo-contact-hero"), {"overflow": "hidden"},
        pad=(70, 24, 46, 24), pad_mobile=(48, 16, 32, 16))

    # ---- form card (spans 2 rows) | image | help box
    form = widget("form", {
        "form_name": "Contact Form",
        "form_fields": [
            {"_id": eid(), "custom_id": "name", "field_type": "text", "field_label": "Your Name",
             "placeholder": "Enter your name", "required": "true", "width": "100"},
            {"_id": eid(), "custom_id": "email", "field_type": "email", "field_label": "Email Address",
             "placeholder": "Enter your email address", "required": "true", "width": "100"},
            {"_id": eid(), "custom_id": "topic", "field_type": "select", "field_label": "Topic",
             "field_options": "Please select a topic|\nProduct questions\nOrder enquiries\nShipping information\nSomething else",
             "required": "true", "width": "100"},
            {"_id": eid(), "custom_id": "order_number", "field_type": "text", "field_label": "Order Number (optional)",
             "placeholder": "Enter order number (optional)", "width": "100"},
            {"_id": eid(), "custom_id": "message", "field_type": "textarea", "field_label": "Message",
             "placeholder": "Tell us how we can help...", "required": "true", "width": "100", "rows": 5},
        ],
        "input_size": "md", "show_labels": "yes", "mark_required": "",
        "button_text": "Send Message", "button_size": "md", "button_width": "100",
        "submit_actions": ["email"], "email_subject": "New message from the Be Organic contact form",
        "success_message": "Thank you! We’ll get back to you within one business day.",
        "column_gap": px(0), "row_gap": px(22), "label_spacing": px(9),
        "field_border_width": dims(1), "field_border_radius": dims(4),
        "button_border_radius": dims(6), "button_text_padding": dims(19, 24, 19, 24),
    }, typo("label_typography", "text"), typo("field_typography", "bosmall"), typo("button_typography", "accent"),
        {"label_typography_font_size": px(16)},
        {"__globals__": {"label_color": gcol("boink"), "field_text_color": gcol("boink"),
                         "field_background_color": gcol("bowhite"), "field_border_color": gcol("boborder"),
                         "button_background_color": gcol("primary"), "button_text_color": gcol("bowhite"),
                         "button_background_hover_color": gcol("bodeep"), "button_hover_color": gcol("bowhite")}},
        css_class("bo-form"),
        custom_css("selector .elementor-field-type-submit{margin-top:6px}"))

    form_card = flex([
        heading("Send us a message", "h2", "boh3"),
        form,
    ], "column", 22, bg_color("bopaper"),
        border(1, "boborder", radius=6),
        {"padding": dims(34, 32, 32, 32), "padding_mobile": dims(26, 20, 24, 20),
         "grid_row": "2", "grid_row_mobile": "1"},
        css_class("bo-form-card"))

    photo = image(img("contact-moringa-pouch"), "Be Organic moringa powder with a cup of matcha-style moringa drink",
                  552, 6, {"_grid_row": ""}, height_tablet=440, height_mobile=300)

    help_list = widget("icon-list", {
        "view": "traditional",
        "icon_list": [{"_id": eid(), "text": t, "selected_icon": {"value": "", "library": ""},
                       "link": {"url": u, "is_external": "", "nofollow": ""}}
                      for t, u in [("Product questions", "#faq"), ("Order enquiries", "#faq"),
                                   ("Shipping information", "#faq")]],
        "space_between": px(0), "divider": "yes", "divider_style": "solid", "divider_weight": px(1),
        "divider_width": px(100, "%"),
    }, typo("icon_typography", "bolead"), {"divider_color": "#1F3D2B33"},
        {"__globals__": {"text_color": gcol("boink"), "text_color_hover": gcol("primary")}},
        css_class("bo-help-list"),
        custom_css(f"""
selector .elementor-icon-list-item{{padding:13px 0!important}}
selector .elementor-icon-list-item:first-child{{padding-top:6px!important}}
selector .elementor-icon-list-item:last-child{{padding-bottom:4px!important}}
selector .elementor-icon-list-item>a{{display:flex;width:100%;align-items:center;justify-content:space-between}}
selector .elementor-icon-list-item>a::after{{content:"";width:16px;height:12px;flex:0 0 auto;{mask(ARROW)}color:{C('boink')};transition:transform .25s ease}}
selector .elementor-icon-list-item>a:hover::after{{transform:translateX(4px)}}
selector .elementor-icon-list-item:not(:last-child):after{{left:0;width:100%}}
"""))
    help_box = flex([
        heading("How can we help?", "h2", "boh3"),
        help_list,
    ], "column", 12, bg_color("accent"), {"border_radius": dims(6),
                                          "padding": dims(30, 56, 26, 56), "padding_tablet": dims(28, 32, 24, 32),
                                          "padding_mobile": dims(24, 20, 20, 20)})

    main = section([
        grid([form_card, photo, help_box], "1fr 1fr", 16, 18, cols_tablet="1fr 1fr", cols_mobile="1fr",
             inner=True, rows="auto auto"),
    ], pad=(0, 24, 26, 24), pad_mobile=(0, 16, 24, 16))

    # ---- FAQ
    faq_items = [
        ("How can I use the powders?",
         "Our powders are easy to add to your daily routine. From smoothies and oat bowls to baking and simple drinks, "
         "there are many ways to enjoy them. Visit our product pages for serving ideas and inspiration."),
        ("Where can I find ingredient details?",
         "Every product page lists the full ingredient details, origin and nutrition information. You’ll also find "
         "the same details printed on the back of each pouch."),
        ("How do I check shipping options?",
         "Shipping options and delivery times are shown at checkout once you enter your address. For anything else, "
         "send us a message and we’ll be happy to help."),
    ]
    acc_children = []
    for i, (_q, a) in enumerate(faq_items, 1):
        acc_children.append(container([
            text(f"<p>{a}</p>", "bosmall", "text", None, {"typography_font_size": px(16)}),
        ], {"_title": f"item #{i}", "content_width": "full", "container_type": "flex",
            "flex_direction": "column"}, inner=True))
    accordion = {
        "id": eid(), "elType": "widget", "isInner": False, "widgetType": "nested-accordion",
        "settings": merge({
            "items": [{"_id": eid(), "item_title": q, "element_css_id": ""} for q, _a in faq_items],
            "accordion_item_title_position_horizontal": "stretch",
            "accordion_item_title_icon_position": "end",
            "accordion_item_title_icon": fa("fas fa-chevron-down"),
            "accordion_item_title_icon_active": fa("fas fa-chevron-up"),
            "title_tag": "h3", "faq_schema": "yes", "default_state": "expanded", "max_items_expended": "one",
            "accordion_item_title_space_between": px(10),
            "accordion_item_title_distance_from_content": px(0),
            "accordion_padding": dims(19, 26, 19, 26),
            "accordion_border_radius": dims(4),
            "accordion_background_normal_background": "classic",
            "accordion_background_hover_background": "classic",
            "accordion_background_active_background": "classic",
            "accordion_border_normal_border": "solid", "accordion_border_normal_width": dims(1),
            "accordion_border_hover_border": "solid", "accordion_border_hover_width": dims(1),
            "accordion_border_active_border": "solid", "accordion_border_active_width": dims(1, 1, 0, 1),
            "content_background_background": "classic",
            "content_border_border": "solid", "content_border_width": dims(0, 1, 1, 1),
            "content_border_radius": dims(0, 0, 4, 4),
            "content_padding": dims(0, 26, 24, 26),
            "icon_size": px(15), "icon_spacing": px(16),
        }, typo("title_typography", "boh5"),
            {"__globals__": {
                "accordion_background_normal_color": gcol("bowhite"),
                "accordion_background_hover_color": gcol("bowhite"),
                "accordion_background_active_color": gcol("bowhite"),
                "accordion_border_normal_color": gcol("boborder"),
                "accordion_border_hover_color": gcol("boborder"),
                "accordion_border_active_color": gcol("boborder"),
                "content_background_color": gcol("bowhite"),
                "content_border_color": gcol("boborder"),
                "normal_title_color": gcol("boink"), "hover_title_color": gcol("primary"),
                "active_title_color": gcol("boink"),
                "normal_icon_color": gcol("boink"), "hover_icon_color": gcol("primary"),
                "active_icon_color": gcol("boink"),
            }},
            css_class("bo-faq"),
            custom_css("""
selector .e-n-accordion-item[open]>.e-n-accordion-item-title{border-bottom-left-radius:0;border-bottom-right-radius:0}
selector .e-n-accordion-item-title-text{line-height:1.35}
@media (max-width:767px){selector .e-n-accordion-item-title{padding:16px 18px!important}selector .e-n-accordion-item>[role=region]{padding:0 18px 18px!important}}
""")),
        "elements": acc_children,
    }

    faq_left = flex([
        heading("A few helpful answers", "h2", "secondary"),
        accordion,
    ], "column", 18, {"padding": dims(26, 0, 0, 10), "padding_mobile": dims(0)})
    faq = section([
        grid([faq_left, image(img("contact-faq-turmeric"), "Turmeric powder in a ceramic bowl with fresh turmeric roots",
                              445, 6, height_tablet=380, height_mobile=260)],
             "1.19fr 1fr", 28, 24, {"grid_align_items": "start"}, cols_tablet="1fr", cols_mobile="1fr", inner=True),
    ], bg_color("bopaper"), {"_element_id": "faq"},
        pad=(20, 24, 14, 24), pad_mobile=(40, 16, 32, 16))

    # ---- newsletter strip
    news_text = flex([
        heading("Join our journey", "p", "boeyebrow", "boink", None, None, {"typography_font_size": px(11)}),
        image_box("Get the latest inspiration", "Sign up for simple ideas, new products and more.", "h2",
                  "secondary", "bolead", "boink", "boink", "left", 12, {"description_typography_font_size": px(17)},
                  align_mobile="left"),
    ], "column", 8)
    news = section([
        html(leaf_branch(200, flip=False, rotate=-28, seed=3),
             {"_position": "absolute", "_offset_orientation_h": "start", "_offset_x": px(-10),
              "_offset_orientation_v": "end", "_offset_y_end": px(-18), "_element_width": "initial",
              "_element_custom_width": px(190)}, hide(tablet=True, mobile=True)),
        grid([news_text, _newsletter_form("Contact Newsletter", "Subscribe", "primary", "66", "34")],
             "1fr 0.82fr", 24, 40, {"grid_align_items": "center", "padding": dims(0, 0, 0, 186),
                                    "padding_tablet": dims(0)},
             cols_tablet="1fr", cols_mobile="1fr", inner=True),
    ], bg_color("accent"), {"overflow": "hidden"}, pad=(34, 24, 32, 24), pad_mobile=(36, 16, 36, 16))

    page_css = BASE + FORM + f"""
/* Contact page: gold announcement bar (mockup) */
.bo-topbar{{background-color:{C('secondary')}!important}}
.bo-leaves{{pointer-events:none}}
""" + "\n" + _fallback()
    return [hero, main, faq, news], _page_settings(page_css)


# =====================================================================
# LOOP ITEMS (dynamic cards)
# =====================================================================
def loop_card():
    """Story card used by the Did You Know grid and 'Keep exploring'."""
    reset_ids("loop-card")
    card = container([
        widget("theme-post-featured-image", {
            "image_size": "medium_large", "width": px(100, "%"), "height": px(245), "height_tablet": px(230),
            "height_mobile": px(220), "object-fit": "cover", "object-position": "center center",
            "link_to": "custom", "align": "center",
        }, {"__dynamic__": {"image": tag("post-featured-image"), "link": tag("post-url")}},
            {"_margin": dims(0, 0, 16, 0)}, css_class("bo-card-img")),
        widget("theme-post-title", {"title": "Post Title", "header_size": "h3"},
               {"__dynamic__": {"title": tag("post-title"), "link": tag("post-url")}},
               typo("typography", "boh4"), color("title_color", "boink"), {"_margin": dims(0, 0, 10, 0)},
               css_class("bo-card-title"),
               custom_css(f"selector a:hover{{color:{C('primary')}}}")),
        widget("text-editor", {"editor": "Post excerpt"},
               {"__dynamic__": {"editor": tag("post-excerpt", {"max_length": "26"})}},
               typo("typography", "bosmall"), color("text_color", "bomuted"),
               {"typography_font_size": px(16), "_margin": dims(0, 0, 14, 0), "paragraph_spacing": px(0)},
               css_class("bo-clamp-3")),
        button("Read Story", "#", "text-gold", False, None, False,
               css_class("bo-arrow"), {"typography_font_size": px(16), "typography_typography": "custom"},
               dynamic_link=tag("post-url")),
    ], {"container_type": "flex", "content_width": "full", "flex_direction": "column",
        "flex_gap": gaps(0), "padding": dims(0), "height": "full"}, css_class("bo-card"))
    return [card], {"custom_css": BASE + "\n" + _fallback(), "preview_type": "single/post"}


def loop_spotlight():
    """Large 'Ingredient spotlight' card (latest story) for Did You Know."""
    reset_ids("loop-spotlight")
    body = flex([
        heading("Ingredient spotlight", "p", "boeyebrow", "secondary"),
        widget("theme-post-title", {"title": "Post Title", "header_size": "h2"},
               {"__dynamic__": {"title": tag("post-title"), "link": tag("post-url")}},
               typo("typography", "boh3"), color("title_color", "boink"),
               {"typography_typography": "custom", "typography_font_size": px(34),
                "typography_font_size_mobile": px(27)}),
        widget("text-editor", {"editor": "Post excerpt"},
               {"__dynamic__": {"editor": tag("post-excerpt", {"max_length": "40"})}},
               typo("typography", "text"), color("text_color", "text"), {"paragraph_spacing": px(0)}),
        button("Read Story", "#", "gold", False, None, False, css_class("bo-arrow"),
               {"_margin": dims(8, 0, 0, 0), "text_padding": dims(14, 26, 14, 26), "border_radius": dims(2)},
               dynamic_link=tag("post-url")),
    ], "column", 14, bg_color("bopaper"),
        {"padding": dims(30, 36, 30, 36), "padding_mobile": dims(26, 20, 28, 20)},
        justify="center")
    card = grid([
        widget("theme-post-featured-image", {
            "image_size": "large", "width": px(100, "%"), "height": px(345), "height_tablet": px(300),
            "height_mobile": px(240), "object-fit": "cover", "object-position": "center center",
            "link_to": "custom", "align": "center",
        }, {"__dynamic__": {"image": tag("post-featured-image"), "link": tag("post-url")}}),
        body,
    ], "1.43fr 1fr", 0, 0, {"grid_align_items": "stretch"}, cols_tablet="1fr 1fr", cols_mobile="1fr",
        inner=False)
    return [card], {"custom_css": BASE + "\n" + _fallback(), "preview_type": "single/post"}


def _loop_grid(template_id, per_page, cols, offset=0, query="post", extra=None, cols_tablet="2",
               gap_col=24, gap_row=34):
    s = {
        "template_id": str(template_id), "_skin": "post",
        "columns": str(cols), "columns_tablet": cols_tablet, "columns_mobile": "1",
        "posts_per_page": per_page, "masonry": "", "equal_height": "yes",
        "post_query_post_type": query, "post_query_orderby": "post_date", "post_query_order": "desc",
        "post_query_ignore_sticky_posts": "yes",
        "column_gap": px(gap_col), "row_gap": px(gap_row), "row_gap_mobile": px(30),
        "pagination_type": "",
    }
    if offset:
        s["post_query_offset"] = offset
    return widget("loop-grid", s, extra or {})


# =====================================================================
# DID YOU KNOW PAGE
# =====================================================================
def did_you_know_page():
    reset_ids("did-you-know")
    intro = section([
        heading("Did you know?", "p", "boeyebrow", "secondary", "center"),
        image_box("Every ingredient has a story.",
                  "Explore the origins, flavors, and everyday uses of plant-based powders.",
                  "h1", "primary", "bolead", "boink", "text", "center", 14,
                  {"description_typography_font_size": px(18)}),
    ], {"flex_align_items": "center"}, gap=16, pad=(52, 24, 30, 24), pad_mobile=(40, 16, 24, 16))

    spotlight = section([
        _loop_grid(SPOTLIGHT_TEMPLATE_ID, 1, 1, 0, extra={"columns_tablet": "1"}),
    ], pad=(0, 24, 0, 24), pad_mobile=(0, 16, 0, 16))

    grid_id_holder = {}
    stories = _loop_grid(CARD_TEMPLATE_ID, 6, 3, 1, extra=css_class("bo-stories"))
    grid_id_holder["id"] = stories["id"]

    tax_filter = widget("taxonomy-filter", {
        "selected_element": stories["id"], "taxonomy": "category",
        "first_item_title": "All Stories", "show_first_item": "yes",
        "horizontal_scroll": "", "multiple_selection": "",
        "align_items": "center",
        "space_between_items": px(14),
    }, typo("taxonomy_filter_normal_typography", "bosmall"),
        css_class("bo-filter"),
        custom_css(f"""
selector .e-filter{{justify-content:center;gap:14px;flex-wrap:wrap}}
selector .e-filter-item{{font-family:{F('bosmall')},sans-serif;font-size:15px;line-height:1;padding:12px 24px;border-radius:40px;border:1px solid {C('boink')};background:transparent;color:{C('boink')};cursor:pointer;transition:all .2s ease}}
selector .e-filter-item:hover{{border-color:{C('primary')};color:{C('primary')}}}
selector .e-filter-item[aria-pressed=true]{{background:{C('primary')};border-color:{C('primary')};color:{C('bowhite')}}}
"""))

    stories_sec = section([tax_filter, stories], gap=28, pad=(28, 24, 70, 24), pad_mobile=(24, 16, 50, 16))

    cta = section([
        image_box("Curious to try something new?",
                  "Explore our range of organic plant powders and find your next kitchen favorite.",
                  "h2", "secondary", "text", "boink", "text", "left", 18,
                  {"_element_width": "initial", "_element_custom_width": px(400),
                   "_element_width_mobile": "inherit"}),
        button("Shop Powders", SHOP_URL, "dark", False, None, False, css_class("bo-arrow"),
               {"_margin": dims(8, 0, 0, 0), "text_padding": dims(16, 28, 16, 28), "border_radius": dims(2)}),
    ], {"background_background": "classic",
        "background_image": {"url": img("cta-powder-pouches"), "id": "", "source": "library", "alt": ""},
        "background_position": "center right", "background_repeat": "no-repeat",
        "background_size": "initial", "background_bg_width": px(70, "%"),
        "background_position_mobile": "bottom center", "background_bg_width_mobile": px(100, "%"),
        "background_overlay_background": "gradient",
        "background_overlay_color_stop": px(30, "%"), "background_overlay_color_b": "#DCE3D300",
        "background_overlay_color_b_stop": px(46, "%"),
        "background_overlay_gradient_type": "linear", "background_overlay_gradient_angle": px(90, "deg"),
        "background_overlay_gradient_angle_mobile": px(180, "deg"),
        "background_overlay_color_stop_mobile": px(58, "%"), "background_overlay_color_b_stop_mobile": px(72, "%"),
        "min_height_mobile": px(0),
        "min_height": px(340), "flex_justify_content": "center"},
        {"__globals__": {"background_color": gcol("accent"), "background_overlay_color": gcol("accent")}},
        {"background_color": "#DCE3D3"},
        css_class("bo-cta"), gap=10, full=False,
        pad=(44, 24, 44, 24), pad_mobile=(44, 16, 175, 16))

    page_css = BASE + "\n" + _fallback()
    return [intro, spotlight, stories_sec, cta], _page_settings(page_css)


# =====================================================================
# SINGLE POST (Theme Builder)
# =====================================================================
def single_post():
    reset_ids("single-post")
    crumbs = flex([
        text(f'<p><a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="{DYK_URL}">Did You Know</a>&nbsp;&nbsp;/&nbsp;&nbsp;</p>',
             "bosmall", "bomuted", None, {"typography_font_size": px(13), "_element_width": "auto"},
             css_class("bo-crumbs")),
        widget("theme-post-title", {"title": "Post Title", "header_size": "span"},
               {"__dynamic__": {"title": tag("post-title")}},
               typo("typography", "bosmall"), color("title_color", "bomuted"),
               {"typography_typography": "custom", "typography_font_size": px(13), "_element_width": "auto"},
               css_class("bo-crumb-current")),
    ], "row", 0, align="center", justify="flex-start", wrap="wrap",
        *[{"_element_width": "full", "margin": dims(0, 0, 14, 0)},
          custom_css(f"selector a{{color:{C('bomuted')}}} selector a:hover{{color:{C('primary')}}}"
                     "selector .elementor-widget-text-editor p{margin:0}")])

    meta = flex([
        html('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
             'stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
             css_class("bo-meta-icon"), {"_element_width": "auto"}),
        heading("By Be Organic", "span", "bosmall", "boink", None, None,
                {"typography_typography": "custom", "typography_font_size": px(14), "_element_width": "auto"},
                dynamic=tag("author-name", {"before": "By "})),
        heading("•", "span", "bosmall", "bomuted", None, None, {"_element_width": "auto"}),
        heading("5 min read", "span", "bosmall", "boink", None, None,
                {"typography_typography": "custom", "typography_font_size": px(14), "_element_width": "auto"},
                dynamic=tag("post-custom-field", {"key": "", "custom_key": "bo_read_time", "fallback": "5 min read"})),
    ], "row", 10, align="center", justify="center", wrap="wrap",
        *[custom_css(f"selector .bo-meta-icon{{color:{C('boink')};line-height:0}}")])

    intro = section([
        crumbs,
        widget("heading", {"title": "Ingredient Spotlight", "header_size": "p", "align": "center"},
               {"__dynamic__": {"title": tag("post-custom-field", {"key": "", "custom_key": "bo_eyebrow", "fallback": "Did You Know"})}},
               typo("typography", "boeyebrow"), color("title_color", "secondary")),
        widget("theme-post-title", {"title": "Post Title", "header_size": "h1", "align": "center"},
               {"__dynamic__": {"title": tag("post-title")}},
               typo("typography", "primary"), color("title_color", "boink"),
               {"typography_typography": "custom", "typography_font_size": px(48),
                "typography_font_size_tablet": px(42), "typography_font_size_mobile": px(34),
                "_element_width": "initial", "_element_custom_width": px(560, "px"),
                "_element_width_mobile": "inherit", "_flex_align_self": "center"}),
        heading("A closer look at this golden kitchen staple.", "p", "bolead", "boink", "center", None,
                dynamic=tag("post-custom-field", {"key": "", "custom_key": "bo_subtitle", "fallback": ""})),
        meta,
        widget("theme-post-featured-image", {
            "image_size": "full", "width": px(100, "%"), "height": px(480), "height_tablet": px(400),
            "height_mobile": px(260), "object-fit": "cover", "object-position": "center center",
            "align": "center",
        }, {"__dynamic__": {"image": tag("post-featured-image")}}, {"_margin": dims(14, 0, 0, 0)}),
    ], {"flex_align_items": "stretch"}, gap=10, pad=(16, 24, 30, 24), pad_mobile=(14, 16, 24, 16))

    content = widget("theme-post-content", {}, typo("typography", "text"), color("text_color", "text"),
                     css_class("bo-post-content"),
                     custom_css(f"""
selector h2{{font-family:{F('boh3')},serif;font-weight:500;font-size:30px;line-height:1.2;color:{C('boink')};margin:30px 0 12px}}
selector h2:first-child{{margin-top:0}}
selector h3{{font-family:{F('boh4')},serif;font-weight:500;font-size:24px;line-height:1.25;color:{C('boink')};margin:26px 0 10px}}
selector p{{margin:0 0 16px}}
selector ul{{list-style:none;margin:0 0 22px;padding:0}}
selector ul li{{position:relative;padding-left:24px;margin-bottom:10px}}
selector ul li::before{{content:"";position:absolute;left:2px;top:.62em;width:8px;height:8px;border-radius:50%;background:{C('secondary')}}}
selector strong{{color:{C('boink')};font-weight:500}}
selector img,selector figure img{{width:100%;height:auto;border-radius:0;display:block}}
selector figure{{margin:26px 0 22px}}
selector a{{color:{C('bogold')};text-decoration:underline;text-underline-offset:3px}}
@media (max-width:767px){{selector h2{{font-size:26px}}}}
"""))

    toc = widget("table-of-contents", {
        "title": "In this article", "html_tag": "h3", "headings_by_tags": ["h2"],
        "container": ".bo-post-content", "marker_view": "bullets",
        "icon": {"value": "", "library": ""}, "hierarchical_view": "", "collapse_subitems": "",
        "minimize_box": "", "no_headings_message": "Scroll to read the full story.",
    }, css_class("bo-toc"),
        custom_css(f"""
selector{{--box-background-color:transparent;--box-border-width:0px;--box-border-color:transparent;--box-padding:0px;--box-border-radius:0px;--header-background-color:transparent;--header-color:{C('boink')};--separator-width:0px;--item-text-color:{C('text')};--item-text-hover-color:{C('primary')};--marker-color:transparent;--marker-size:0px;--toc-body-max-height:none}}
selector .elementor-toc{{background:transparent;border:0;padding:0}}
selector .elementor-toc__header{{padding:0 0 14px;border:0;background:transparent;display:flex;align-items:flex-start;justify-content:space-between}}
selector .elementor-toc__header-title{{font-family:{F('boh4')},serif;font-weight:500;font-size:25px;line-height:1.2;color:{C('boink')}}}
selector .elementor-toc__header::after{{content:"";width:22px;height:28px;flex:0 0 auto;margin-left:12px;background-color:{C('boink')};-webkit-mask:var(--bo-sprig) center/contain no-repeat;mask:var(--bo-sprig) center/contain no-repeat}}
selector .elementor-toc__body{{padding:0;max-height:none}}
selector .elementor-toc__list-wrapper{{margin:0;padding:0;list-style:none}}
selector .elementor-toc__list-item{{margin:0 0 12px;font-family:{F('bosmall')},sans-serif;font-size:15px;line-height:1.45}}
selector .elementor-toc__list-item-text-wrapper::before,selector .elementor-toc__list-item-text-wrapper i{{display:none}}
selector .elementor-toc__list-item-text{{color:{C('text')}}}
selector .elementor-toc__list-item-text:hover,selector .elementor-toc__list-item-text.elementor-item-active{{color:{C('primary')};text-decoration:none}}
selector .elementor-toc__toggle-button{{display:none!important}}
"""))

    toc_box = flex([toc], "column", 0, bg_color("accent"),
                   {"padding": dims(30, 26, 18, 26), "border_radius": dims(0)})
    cta_box = flex([
        flex([
            image_box("Bring a little color to your kitchen.", "", "h3", "boh4", "text", "boink", "text",
                      "left", 0, {"title_typography_font_size": px(24), "title_typography_typography": "custom"}),
            html(sprig_icon(26), {"_element_width": "auto", "_flex_align_self": "flex-start"},
                 css_class("bo-cta-sprig")),
        ], "row", 10, align="flex-start", justify="space-between", wrap="nowrap",
            *[custom_css(f"selector .bo-cta-sprig{{color:{C('boink')};line-height:0}}")]),
        text("<p>Explore our range of organic plant powders and find your next kitchen favorite.</p>", "bosmall",
             "text", None, {"typography_font_size": px(15)}),
        button("Shop Powders", SHOP_URL, "dark", False, None, False, css_class("bo-arrow"),
               {"_margin": dims(6, 0, 0, 0), "text_padding": dims(14, 24, 14, 24), "border_radius": dims(0),
                "typography_typography": "custom", "typography_font_size": px(15)}),
    ], "column", 12, bg_color("accent"), {"padding": dims(28, 26, 30, 26)})

    sidebar = flex([toc_box, cta_box], "column", 14,
                   {"sticky": "top", "sticky_on": ["desktop"], "sticky_offset": 30, "sticky_parent": "yes",
                    "sticky_effects_offset": 0})

    share = flex([
        heading("Share this story", "span", "bosmall", "boink", None, None,
                {"typography_typography": "custom", "typography_font_size": px(14), "typography_font_weight": "500",
                 "_element_width": "auto", "_margin": dims(0, 10, 0, 0)}),
        widget("share-buttons", {
            "share_buttons": [{"_id": eid(), "button": "facebook"}, {"_id": eid(), "button": "pinterest"}],
            "view": "icon", "skin": "flat", "shape": "circle", "columns": "0", "alignment": "left",
            "color_source": "custom", "button_size": px(1), "icon_size": em(1.05), "column_gap": px(10),
            "primary_color": "#E9E6DF", "secondary_color": "#16291E",
        }, {"_element_width": "auto"}, css_class("bo-share"),
            custom_css(f"""
selector .elementor-share-btn{{width:38px!important;height:38px!important;border-radius:50%;background-color:#E9E6DF!important}}
selector .elementor-share-btn__icon{{width:38px}}
selector .elementor-share-btn__icon i,selector .elementor-share-btn__icon svg{{color:{C('boink')}!important;fill:{C('boink')}!important;font-size:15px}}
selector .elementor-share-btn:hover{{background-color:{C('accent')}!important}}
""")),
        html('<button type="button" class="bo-copy" aria-label="Copy link" '
             'onclick="navigator.clipboard&&navigator.clipboard.writeText(window.location.href);this.classList.add(\'is-done\');var b=this;setTimeout(function(){b.classList.remove(\'is-done\')},1600)">'
             '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M10 13a5 5 0 0 0 7.07 0l3-3a5 5 0 0 0-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 0 0-7.07 0l-3 3a5 5 0 0 0 7.07 7.07l1.5-1.5"/></svg>'
             '<span class="bo-copy__tip">Copied!</span></button>',
             {"_element_width": "auto"},
             custom_css(f"""
selector .bo-copy{{position:relative;width:38px;height:38px;border-radius:50%;border:0;background:#E9E6DF;color:{C('boink')};display:inline-flex;align-items:center;justify-content:center;padding:0;cursor:pointer;transition:background .2s}}
selector .bo-copy:hover,selector .bo-copy:focus{{background:{C('accent')};color:{C('boink')}}}
selector .bo-copy__tip{{position:absolute;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);font-size:12px;background:{C('primary')};color:#fff;padding:3px 8px;border-radius:3px;opacity:0;pointer-events:none;transition:opacity .2s;white-space:nowrap}}
selector .bo-copy.is-done .bo-copy__tip{{opacity:1}}
""")),
    ], "row", 8, align="center", justify="flex-start", wrap="wrap")

    share_row = grid([
        share,
        button("Back to All Stories", DYK_URL, "text-gold", False, {"align": "right", "align_mobile": "left"},
               False, css_class("bo-arrow-left"),
               {"typography_typography": "custom", "typography_font_size": px(15)}),
    ], "1fr auto", 16, 20, {"grid_align_items": "center", "border_border": "solid",
                            "border_width": dims(1, 0, 0, 0), "padding": dims(18, 0, 0, 0)},
        {"__globals__": {"border_color": gcol("boborder")}}, cols_mobile="1fr")

    main_col = flex([content, share_row], "column", 26)

    body = section([
        grid([main_col, sidebar], "2.15fr 1fr", 36, 30, {"grid_align_items": "start"},
             cols_tablet="1fr", cols_mobile="1fr", inner=True),
    ], pad=(18, 24, 40, 24), pad_mobile=(10, 16, 32, 16))

    keep = section([
        widget("divider", {"style": "solid", "weight": px(1), "look": "line_text", "text": "Keep exploring",
                           "html_tag": "h2", "align": "center", "gap": px(2), "text_align": "center",
                           "text_spacing": px(24), "width": px(100, "%")},
               typo("typography", "boh4"), {"__globals__": {"color": gcol("secondary"), "text_color": gcol("boink")}},
               {"typography_typography": "custom", "typography_font_size": px(26)},
               custom_css("selector .elementor-divider-separator{opacity:.55}")),
        _loop_grid(CARD_TEMPLATE_ID, 3, 3, 0, query="related",
                   extra={"post_query_related_taxonomies": ["category"],
                          "post_query_related_fallback": "fallback_recent",
                          "post_query_exclude": ["current_post"]}),
    ], gap=26, pad=(10, 24, 56, 24), pad_mobile=(10, 16, 44, 16))

    news = section([
        grid([
            image_box("Get inspired, naturally.", "Get simple ideas, new recipes and updates straight to your inbox.",
                      "h2", "boh3", "bosmall", "boink", "text", "left", 10,
                      {"description_typography_font_size": px(16)}),
            _newsletter_form("Blog Newsletter", "Subscribe", "secondary", "66", "34"),
            html(leaf_outline_art(104), {"_element_width": "auto"}, hide(mobile=True),
                 custom_css(f"selector .bo-leaf-outline{{color:{C('boink')};display:block}}")),
        ], "1fr 1.05fr 120px", 24, 48, {"grid_align_items": "center"},
            cols_tablet="1fr 1fr", cols_mobile="1fr", inner=True),
    ], bg_color("accent"), pad=(30, 24, 30, 24), pad_mobile=(36, 16, 36, 16))

    sprig_svg = sprig_icon(22, "black").replace('"', "'")
    from urllib.parse import quote
    page_css = BASE + FORM + f"""
.elementor-location-single{{--bo-sprig:url("data:image/svg+xml,{quote(sprig_svg, safe="=:/' ")}")}}
""" + "\n" + _fallback()
    return [intro, body, keep, news], {"custom_css": page_css, "preview_type": "single/post"}


# =====================================================================
def _page_settings(css):
    return {
        "template": "elementor_header_footer",
        "hide_title": "yes",
        "background_background": "classic",
        "background_color": "#F8F4EE",
        "__globals__": {"background_color": "globals/colors?id=bocream"},
        "custom_css": css,
    }


def _fallback():
    from theme import fallback_css
    return "/* Fallback values - Site Settings (global colors/fonts) override these */\n" + fallback_css()
