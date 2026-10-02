"""Shared CSS snippets. Colors/fonts always go through the global variables so
changing Site Settings re-themes every page."""
from urllib.parse import quote

ARROW_SVG = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 12'><path d='M1 6h13M9.5 1.5 14 6l-4.5 4.5' "
             "fill='none' stroke='black' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'/></svg>")
ARROW = "url(\"data:image/svg+xml," + quote(ARROW_SVG, safe="=:/' ") + "\")"

CHEVRON_SVG = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 10'><path d='M1.5 1.5 8 8l6.5-6.5' "
               "fill='none' stroke='black' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'/></svg>")
CHEVRON = "url(\"data:image/svg+xml," + quote(CHEVRON_SVG, safe="=:/' ") + "\")"

C = lambda cid: f"var(--e-global-color-{cid})"  # noqa: E731
F = lambda tid: f"var(--e-global-typography-{tid}-font-family)"  # noqa: E731


def mask(url):
    return (f"background-color:currentColor;-webkit-mask:{url} center/contain no-repeat;"
            f"mask:{url} center/contain no-repeat;")


BASE = f"""
/* ===== Be Organic base helpers ===== */
.bo-arrow .elementor-button-content-wrapper::after{{content:"";display:inline-block;flex:0 0 auto;width:15px;height:11px;margin-inline-start:10px;{mask(ARROW)}transition:transform .25s ease}}
.bo-arrow .elementor-button:hover .elementor-button-content-wrapper::after{{transform:translateX(4px)}}
.bo-arrow-left .elementor-button-content-wrapper::before{{content:"";display:inline-block;flex:0 0 auto;width:15px;height:11px;margin-inline-end:10px;{mask(ARROW)}transform:scaleX(-1);transition:transform .25s ease}}
.bo-arrow-left .elementor-button:hover .elementor-button-content-wrapper::before{{transform:scaleX(-1) translateX(4px)}}
.bo-arrow .elementor-button,.bo-arrow-left .elementor-button{{transition:background-color .25s ease,color .25s ease}}
.bo-leaf-art{{display:block;max-width:100%;height:auto}}
body a.bo-logo,.bo-logo{{display:inline-flex;align-items:flex-end;gap:6px;text-decoration:none;color:{C('boink')};font-family:{F('bologo')},serif;font-weight:var(--e-global-typography-bologo-font-weight);font-size:var(--e-global-typography-bologo-font-size);letter-spacing:var(--e-global-typography-bologo-letter-spacing);line-height:1;text-transform:uppercase;white-space:nowrap}}
body a.bo-logo:hover{{color:{C('boink')}}}
.bo-logo .bo-sprig{{margin-bottom:2px;color:{C('boink')}}}
body a.bo-logo--light,body a.bo-logo--light:hover,.bo-logo--light .bo-sprig{{color:{C('bowhite')}}}
.bo-clamp-3 .elementor-widget-container,.bo-clamp-3>p,.bo-clamp-3 p{{display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}}
"""

# Pro Form styling shared by contact + newsletter forms
FORM = f"""
.bo-form .elementor-field-group .elementor-field-textual,.bo-form .elementor-field-group select{{min-height:50px;padding:12px 16px;border-radius:4px;box-shadow:none;transition:border-color .2s ease}}
.bo-form .elementor-field-group textarea.elementor-field-textual{{min-height:130px;resize:vertical}}
.bo-form .elementor-field-group .elementor-field-textual:focus,.bo-form .elementor-field-group select:focus{{border-color:{C('primary')}!important;outline:none}}
.bo-form .elementor-field-textual::placeholder{{color:{C('bomuted')};opacity:.85}}
.bo-form .elementor-select-wrapper .select-caret-down-wrapper{{right:16px}}
.bo-form .elementor-select-wrapper select{{color:{C('boink')}}}
.bo-form .elementor-field-type-submit .elementor-button{{min-height:58px;width:100%}}
.bo-form .elementor-button .elementor-button-content-wrapper::after{{content:"";display:inline-block;width:15px;height:11px;margin-inline-start:12px;{mask(ARROW)}transition:transform .25s ease}}
.bo-form .elementor-button:hover .elementor-button-content-wrapper::after{{transform:translateX(4px)}}
.bo-form .elementor-message{{font-size:15px;margin-top:12px}}
.bo-form--inline .elementor-form-fields-wrapper{{flex-wrap:nowrap}}
.bo-form--inline .elementor-field-group{{margin-bottom:0}}
.bo-form--inline .elementor-field-group .elementor-field-textual{{border:0;border-radius:4px 0 0 4px;min-height:52px}}
.bo-form--inline .elementor-field-type-submit .elementor-button{{border-radius:0 4px 4px 0;min-height:52px;padding:0 26px}}
.bo-form--noarrow .elementor-button .elementor-button-content-wrapper::after{{display:none}}
@media (max-width:767px){{.bo-form--inline .elementor-field-group{{width:auto!important}}.bo-form--inline .elementor-field-type-email{{flex:1 1 auto}}.bo-form--inline .elementor-field-type-submit{{flex:0 0 auto}}}}
"""
