#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os


AUTHOR = 'Rico Rodriguez'
SITENAME = 'Datamance'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'


TIMEZONE = 'America/New_York'

PLUGIN_PATHS = [
   os.environ['PELICAN_PLUGINS_PATH']
]

PLUGINS = [
    'i18n_subsites',
    # 'assets',
]

DEFAULT_LANG = 'en'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'darkly'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
