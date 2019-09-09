# Copyright (c) 2013 Michael Dowling <mtdowling@gmail.com>
# Copyright (c) 2017 Jared Dillard <jared.dillard@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# This is modified version of sphinx-sitemap extension(https://github.com/jdillard/sphinx-sitemap) for generating
# sitemap.xml file when using sphinx-versioning

import os
import xml.etree.ElementTree as ET
from sphinx.writers.html import HTMLTranslator


def setup(app):
    """Setup connects events to the sitemap builder"""
    app.add_config_value(
        'site_url',
        default=None,
        rebuild=False
    )
    try:
        app.add_config_value(
            'html_baseurl',
            default=None,
            rebuild=False
        )
    except:
        pass

    app.connect('html-page-context', http_page_context)
    app.connect('build-finished', create_sitemap)
    app.oro_current_version = None
    app.sitemap_links = []
    app.locales = []


def get_locales(app, exception):
    for locale_dir in app.builder.config.locale_dirs:
        locale_dir = os.path.join(app.confdir, locale_dir)
        if os.path.isdir(locale_dir):
            for locale in os.listdir(locale_dir):
                if os.path.isdir(os.path.join(locale_dir, locale)):
                    app.locales.append(locale)


def http_page_context(app, pagename, templatename, context, doctree):
    add_html_link(app, pagename)
    save_current_version(app, context)
    save_is_root_build(app, context)


def add_html_link(app, pagename):
    """As each page is built, collect page names for the sitemap"""
    app.sitemap_links.append(pagename + ".html")


def save_current_version(app, context):
    if app.oro_current_version is not None:
        return

    if 'oro_current_version' not in context:
        return

    app.oro_current_version = context['oro_current_version']


def save_is_root_build(app, context):
    if app.sitemap_index_is_root_build is not None:
        return

    if 'scv_is_root' not in context:
        return

    app.sitemap_index_is_root_build = context['scv_is_root']


def create_sitemap(app, exception):
    """Generates the sitemap.xml from the collected HTML page links"""
    site_url = app.builder.config.site_url or app.builder.config.html_baseurl
    if not site_url:
        print("sphinx-sitemap error: neither html_baseurl nor site_url "
              "are set in conf.py. Sitemap not built.")
        return
    if (not app.sitemap_links):
        print("sphinx-sitemap warning: No pages generated for sitemap.xml")
        return

    ET.register_namespace('xhtml', "http://www.w3.org/1999/xhtml")

    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    get_locales(app, exception)

    # Build sitemap for default sphinx-build call
    if app.sitemap_index_is_root_build is False:
        if app.oro_current_version is None:
            print("sphinx-sitemap warning: Can not determine current version. Sitemap not built.")
            return

        version = app.oro_current_version + '/'
    else:
        version = ''

    for link in app.sitemap_links:
        url = ET.SubElement(root, "url")
        if app.builder.config.language is not None:
            ET.SubElement(url, "loc").text = site_url + \
                                             app.builder.config.language + '/' + version + link
            if len(app.locales) > 0:
                for lang in app.locales:
                    linktag = ET.SubElement(
                        url,
                        "{http://www.w3.org/1999/xhtml}link"
                    )
                    linktag.set("rel", "alternate")
                    linktag.set("hreflang", lang)
                    linktag.set("href", site_url + lang + '/' + version + link)
        elif version:
            ET.SubElement(url, "loc").text = site_url + version + link
        else:
            ET.SubElement(url, "loc").text = site_url + link

    filename = app.outdir + "/sitemap.xml"
    ET.ElementTree(root).write(filename,
                               xml_declaration=True,
                               encoding='utf-8',
                               method="xml")
    print("sitemap.xml was generated for URL %s in %s" % (site_url, filename))
