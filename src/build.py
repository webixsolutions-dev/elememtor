"""Build every deliverable into ../dist.

    python3 src/build.py

Outputs
  dist/be-organic-kit.zip            Elementor Kit (Site Settings + all templates + pages)
  dist/templates/*.json              Individual templates (Templates > Saved Templates > Import)
  dist/site-settings.json            Global colors/fonts (for reference)
  dist/be-organic-sample-stories.xml WordPress importer file with the 7 sample stories
"""
import json
import os
import sys
import zipfile
from datetime import datetime
from xml.sax.saxutils import escape

sys.path.insert(0, os.path.dirname(__file__))

import pages  # noqa: E402
from pages import CARD_TEMPLATE_ID, SPOTLIGHT_TEMPLATE_ID, img  # noqa: E402
from theme import kit_settings  # noqa: E402
from content import CATEGORIES, POSTS  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DIST = os.path.join(ROOT, "dist")
DB_VERSION = "0.4"

GENERAL = [{"type": "include", "name": "general", "sub_name": "", "sub_id": ""}]
SINGLE_POST = [{"type": "include", "name": "singular", "sub_name": "post", "sub_id": ""}]

# id, file slug, title, library type, kit doc_type, builder, conditions, location
TEMPLATES = [
    (90001, "header", "Be Organic - Header", "header", "header", pages.header, GENERAL, "header"),
    (90002, "footer", "Be Organic - Footer", "footer", "footer", pages.footer_main, GENERAL, "footer"),
    (90003, "footer-contact", "Be Organic - Footer (Contact page)", "footer", "footer", pages.footer_contact, [], "footer"),
    (CARD_TEMPLATE_ID, "loop-item-story-card", "Be Organic - Loop Item - Story Card", "loop-item", "loop-item",
     pages.loop_card, [], ""),
    (SPOTLIGHT_TEMPLATE_ID, "loop-item-spotlight", "Be Organic - Loop Item - Spotlight", "loop-item", "loop-item",
     pages.loop_spotlight, [], ""),
    (90004, "single-post", "Be Organic - Single Post (Story)", "single-post", "single-post", pages.single_post,
     SINGLE_POST, "single"),
]

PAGES = [
    (90201, "contact", "Contact", pages.contact_page),
    (90202, "did-you-know", "Did You Know", pages.did_you_know_page),
]


def _dump(obj):
    return json.dumps(obj, ensure_ascii=False, indent=1)


def build_templates():
    out = {}
    os.makedirs(os.path.join(DIST, "templates"), exist_ok=True)
    for tid, slug, title, lib_type, doc_type, fn, cond, loc in TEMPLATES:
        content, settings = fn()
        out[tid] = (slug, title, lib_type, doc_type, content, settings, cond, loc)
        data = {"content": content, "page_settings": settings, "version": DB_VERSION, "title": title,
                "type": lib_type}
        with open(os.path.join(DIST, "templates", f"{slug}.json"), "w") as f:
            f.write(_dump(data))
    pg = {}
    for pid, slug, title, fn in PAGES:
        content, settings = fn()
        pg[pid] = (slug, title, content, settings)
        data = {"content": content, "page_settings": settings, "version": DB_VERSION,
                "title": f"Be Organic - {title} Page", "type": "page"}
        with open(os.path.join(DIST, "templates", f"page-{slug}.json"), "w") as f:
            f.write(_dump(data))
    return out, pg


def build_kit(tpls, pgs):
    settings = kit_settings()
    site_settings = {"content": [], "settings": settings, "metadata": []}
    with open(os.path.join(DIST, "site-settings.json"), "w") as f:
        f.write(_dump(site_settings))

    manifest = {
        "name": "be-organic",
        "title": "Be Organic",
        "description": "Be Organic website kit: global colors & fonts, header, footers, Contact page, "
                       "Did You Know page, single story template and loop item cards.",
        "author": "Webix Solutions",
        "version": "3.0",
        "elementor_version": "3.30.0",
        "created": datetime(2026, 10, 2, 12, 0, 0).strftime("%Y-%m-%d %H:%M:%S"),
        "thumbnail": "",
        "site": "",
        "site-settings": {
            "theme": False, "globalColors": True, "globalFonts": True, "themeStyleSettings": True,
            "generalSettings": True, "experiments": False, "customCode": False, "customIcons": False,
            "customFonts": False, "classes": False, "variables": False,
        },
        "templates": {},
        "content": {"page": {}},
        "plugins": [
            {"name": "Elementor", "plugin": "elementor/elementor", "pluginUri": "https://elementor.com/",
             "version": "3.30.0"},
            {"name": "Elementor Pro", "plugin": "elementor-pro/elementor-pro", "pluginUri": "https://elementor.com/",
             "version": "3.30.0"},
        ],
    }
    zpath = os.path.join(DIST, "be-organic-kit.zip")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("site-settings.json", _dump(site_settings))
        for tid, (slug, title, lib_type, doc_type, content, settings, cond, loc) in tpls.items():
            entry = {"title": title, "doc_type": doc_type, "thumbnail": False}
            if loc:
                entry["location"] = loc
            entry["conditions"] = cond
            manifest["templates"][str(tid)] = entry
            z.writestr(f"templates/{tid}.json", _dump({"content": content, "settings": settings, "metadata": []}))
        for pid, (slug, title, content, settings) in pgs.items():
            manifest["content"]["page"][str(pid)] = {"title": title, "excerpt": "", "doc_type": "wp-page",
                                                     "thumbnail": False, "url": f"/{slug}/", "terms": []}
            z.writestr(f"content/page/{pid}.json", _dump({"content": content, "settings": settings, "metadata": []}))
        z.writestr("manifest.json", _dump(manifest))
    return zpath


def build_wxr():
    def cdata(s):
        return "<![CDATA[" + s.replace("]]>", "]]]]><![CDATA[>") + "]]>"

    items = []
    att_id = 95000
    post_id = 95500
    for p in POSTS:
        post_id += 1
        att_id += 1
        url = img(p["image"])
        items.append(f"""
	<item>
		<title>{cdata(p['title'] + ' - image')}</title>
		<link>{escape(url)}</link>
		<dc:creator>{cdata('admin')}</dc:creator>
		<content:encoded>{cdata('')}</content:encoded>
		<excerpt:encoded>{cdata('')}</excerpt:encoded>
		<wp:post_id>{att_id}</wp:post_id>
		<wp:post_date>{cdata(p['date'])}</wp:post_date>
		<wp:post_date_gmt>{cdata(p['date'])}</wp:post_date_gmt>
		<wp:post_name>{cdata(p['image'])}</wp:post_name>
		<wp:status>{cdata('inherit')}</wp:status>
		<wp:post_parent>{post_id}</wp:post_parent>
		<wp:post_type>{cdata('attachment')}</wp:post_type>
		<wp:attachment_url>{cdata(url)}</wp:attachment_url>
	</item>""")
        cat_name = dict(CATEGORIES)[p["cat"]]
        metas = [("_thumbnail_id", str(att_id)), ("bo_subtitle", p["subtitle"]), ("bo_eyebrow", p["eyebrow"]),
                 ("bo_read_time", p["read"])]
        meta_xml = "".join(f"""
		<wp:postmeta>
			<wp:meta_key>{cdata(k)}</wp:meta_key>
			<wp:meta_value>{cdata(v)}</wp:meta_value>
		</wp:postmeta>""" for k, v in metas)
        items.append(f"""
	<item>
		<title>{cdata(p['title'])}</title>
		<link>/{p['slug']}/</link>
		<dc:creator>{cdata('admin')}</dc:creator>
		<content:encoded>{cdata(p['body'])}</content:encoded>
		<excerpt:encoded>{cdata(p['excerpt'])}</excerpt:encoded>
		<wp:post_id>{post_id}</wp:post_id>
		<wp:post_date>{cdata(p['date'])}</wp:post_date>
		<wp:post_date_gmt>{cdata(p['date'])}</wp:post_date_gmt>
		<wp:comment_status>{cdata('closed')}</wp:comment_status>
		<wp:ping_status>{cdata('closed')}</wp:ping_status>
		<wp:post_name>{cdata(p['slug'])}</wp:post_name>
		<wp:status>{cdata('publish')}</wp:status>
		<wp:post_parent>0</wp:post_parent>
		<wp:menu_order>0</wp:menu_order>
		<wp:post_type>{cdata('post')}</wp:post_type>
		<wp:is_sticky>0</wp:is_sticky>
		<category domain="category" nicename="{p['cat']}">{cdata(cat_name)}</category>{meta_xml}
	</item>""")

    cats = "".join(f"""
	<wp:category>
		<wp:term_id>{9600 + i}</wp:term_id>
		<wp:category_nicename>{cdata(slug)}</wp:category_nicename>
		<wp:category_parent>{cdata('')}</wp:category_parent>
		<wp:cat_name>{cdata(name)}</wp:cat_name>
	</wp:category>""" for i, (slug, name) in enumerate(CATEGORIES, 1))

    xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
	xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:wp="http://wordpress.org/export/1.2/"
>
<channel>
	<title>Be Organic</title>
	<link>https://example.com</link>
	<description>Simple ingredients. Everyday inspiration.</description>
	<language>en-US</language>
	<wp:wxr_version>1.2</wp:wxr_version>
	<wp:base_site_url>https://example.com</wp:base_site_url>
	<wp:base_blog_url>https://example.com</wp:base_blog_url>
	<wp:author><wp:author_id>1</wp:author_id><wp:author_login>{cdata('admin')}</wp:author_login><wp:author_email>{cdata('admin@example.com')}</wp:author_email><wp:author_display_name>{cdata('Be Organic')}</wp:author_display_name></wp:author>
{cats}
{''.join(items)}
</channel>
</rss>
"""
    path = os.path.join(DIST, "be-organic-sample-stories.xml")
    with open(path, "w") as f:
        f.write(xml)
    return path


if __name__ == "__main__":
    os.makedirs(DIST, exist_ok=True)
    t, p = build_templates()
    print("kit:", build_kit(t, p))
    print("wxr:", build_wxr())
    for name in sorted(os.listdir(os.path.join(DIST, "templates"))):
        print("template:", name)
