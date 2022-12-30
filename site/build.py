#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment, PackageLoader, select_autoescape




template_env = Environment(
    loader=PackageLoader("site"),
    autoescape=select_autoescape()
)
