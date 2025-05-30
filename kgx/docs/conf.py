# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from operator import attrgetter
from copy import deepcopy

sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'kgx'
copyright = '2021-2024, KGX Authors'
author = 'KGX Authors'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosectionlabel',
    'sphinx_click',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinxcontrib.mermaid',
    'sphinxcontrib.programoutput',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'myst_nb',
    'sphinx_design',
    'matplotlib.sphinxext.plot_directive',
    'sphinx_jinja',
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/common.css', # used everywhere!
    'css/notebooks.css', # when using myst_nb
]


# Options for the linkcheck builder
linkcheck_ignore = [
]


# Napoleon
napoleon_google_docstring = True
napoleon_use_admonition_for_examples = True

# Intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'pydantic': ('https://docs.pydantic.dev/latest', None),
    'jinja2': ('https://jinja.palletsprojects.com/en/latest/', None),
    'numpydantic': ('https://numpydantic.readthedocs.io/en/latest/', None)
}

# myst-nb
nb_render_markdown_format = 'myst'
nb_execution_show_tb = True

# myst
myst_heading_anchors = 3
myst_enable_extensions = [
    "attrs_inline",
    "attrs_block",
    "fieldlist"
]
