"""Configuration file for the Sphinx documentation builder.

This file does only contain a selection of the most common options. For a
full list see the documentation:
http://www.sphinx-doc.org/en/master/config
"""
from __future__ import annotations

import os

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# -- Project information -----------------------------------------------------
project = "nitpick"
copyright = "2019, W. Augusto Andreoli"  # pylint: disable=redefined-builtin # noqa: A001
author = "W. Augusto Andreoli"

# The short X.Y version
version = "0.34.0"
# The full version, including alpha/beta/rc tags
release = version

if os.getenv("GITHUB_ACTIONS") is not None:
    # Tell sphinx-gitref to use the Github branch or tag name if running in a GH
    # action workflow. See https://github.com/wildfish/sphinx-gitref#installation
    gitref_branch = os.environ["GITHUB_REF_NAME"]


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
    "sphinx.ext.autodoc",
    # http://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
    "sphinx.ext.autosummary",
    # https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html#automatically-label-sections
    # https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html
    "sphinx.ext.autosectionlabel",
    # http://www.sphinx-doc.org/en/master/usage/extensions/coverage.html
    "sphinx.ext.coverage",
    # http://www.sphinx-doc.org/en/master/usage/extensions/doctest.html
    "sphinx.ext.doctest",
    # http://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
    "sphinx.ext.extlinks",
    # http://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html
    "sphinx.ext.ifconfig",
    # http://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
    "sphinx.ext.intersphinx",
    # http://www.sphinx-doc.org/en/master/usage/extensions/to do.html
    "sphinx.ext.todo",
    # http://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html
    "sphinx.ext.viewcode",
    # https://github.com/wildfish/sphinx-gitref
    "sphinx_gitref",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-master_doc
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Example configuration for intersphinx: refer to the Python standard library.
# The inventory should be present for each of these URLs in the "objects.inv" file
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_mapping
# Use this to inspect the inventory:
# https://github.com/bskinn/sphobjinv
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "marshmallow": ("https://marshmallow.readthedocs.io/en/stable", None),
    "ruamel.yaml": ("https://yaml.readthedocs.io/en/latest", None),
    "jmespath": ("https://jmespath.readthedocs.io/en/latest", None),
    "configupdater": ("https://configupdater.readthedocs.io/en/latest/", None),
    "pluggy": ("https://pluggy.readthedocs.io/en/latest/", None),
    "click": ("https://click.palletsprojects.com/en/7.x/", None),
}

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-nitpicky
nitpicky = True

# Ignore warning for these classes generated by autodoc,
# but that could not be found in the "intersphinx_mapping" above.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-nitpick_ignore
# If Sphinx generates warnings like this:
#   WARNING: py:class reference target not found: nitpick.enums._OptionMixin
# then add the target to this dict below
nitpick_ignore = [
    (key, identifier)
    for key, identifiers in {
        "py:class": {
            "BaseDoc",
            "bool|tuple",
            "builtins.dict",
            "callable",
            "click.core.Context",
            "Field",
            "FileInfo",
            "flake8.options.manager.OptionManager",
            "jmespath.parser.ParsedResult",
            "JsonDict",
            "ma_fields.Field",
            "marshmallow.base.FieldABC",
            "marshmallow.schema.Schema",
            "marshmallow.schema.SchemaOpts",
            "nitpick.enums._OptionMixin",
            "Path",
            "pluggy.manager.PluginManager",
            "ruamel.yaml.comments.CommentedMap",
            "ruamel.yaml.comments.CommentedSeq",
            "Schema",
            "SchemaOpts",
            "tomlkit.toml_document.TOMLDocument",
            "Tuple[int, ...]",
            "ValidationError",
        },
        "py:exc": {"ValidationError"},
    }.items()
    for identifier in identifiers
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=nitpicky#confval-html_last_updated_fmt
html_last_updated_fmt = ""

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "nitpickdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements: dict[str, str] = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, "nitpick.tex", "nitpick Documentation", "W. Augusto Andreoli", "manual")]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "nitpick", "nitpick Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "nitpick",
        "nitpick Documentation",
        author,
        "nitpick",
        "Enforce the same settings across multiple language-independent projects",
        "Miscellaneous",
    )
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Extension configuration -------------------------------------------------

# http://www.sphinx-doc.org/en/master/usage/extensions/to do.html#confval-todo_include_todos
# If true, `to do` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autoclass_content
autoclass_content = "both"

# http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_default_options
autodoc_default_options = {"members": True, "inherited-members": True, "show-inheritance": True}

# http://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html#confval-autosummary_generate
autosummary_generate = True

# http://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#confval-extlinks
extlinks = {"issue": ("https://github.com/andreoliwa/nitpick/issues/%s", "issue ")}

# https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html#confval-autosectionlabel_prefix_document
autosectionlabel_prefix_document = True
