# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ansible for Network Automation'
copyright = '2024, Syed Asif'
author = 'Syed Asif'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        "myst_parser",
        "sphinx.ext.duration",
        "sphinx.ext.autosectionlabel",
        "sphinx.ext.autodoc",
        ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
...
html_theme = "sphinx_book_theme"
...

# html_logo = "../../python.JPG"
html_title = "Ansible for Network Automation"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']