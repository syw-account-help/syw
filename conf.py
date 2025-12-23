# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'syw.accountonline.com Login'
copyright = '2025, Syw'
author = 'Syw Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

# Allow reStructuredText raw HTML
raw_enabled = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (optional)
# html_theme = 'sphinx_rtd_theme'

# ✅ SEO-Optimized Titles Using Your Keyword
html_title = "SYW Account Online Log In to Account | syw.accountonline.com Login Guide  "
html_short_title = "SYW Account Online Log"

# ✅ Optional: Add Meta Keywords for SEO
html_meta = {
    "description": "Learn how to log in to your SYW account online using syw.accountonline.com login. Step-by-step access, bill payment, password recovery, and troubleshooting tips.",
    "keywords": "syw.accountonline.com login, syw.accountonline.com login official site, syw.accountonline.com pay bill, www.syw.accountonline.com login, syw.accountonline.com login credit card, syw account online log in to account, syw mastercard, syw account online log in, syw account online payment bill"
}

# Favicon
html_favicon = 'favicon.ico'

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML in .rst files (for buttons)
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets
# html_static_path = ['_static']
