import pathlib
import sys

root = pathlib.Path(__file__).parents[2].resolve()
sys.path.insert(0, root.as_posix())

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PRI Bayesian Network'
copyright = '2026, AxelB'
author = 'AxelB'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc', # documentation in code
    'sphinx.ext.viewcode', # link to source
    'sphinx.ext.napoleon', # google style docstrings
    'sphinx_autodoc_typehints', # DRY type hints
    'sphinx_copybutton', # easy copy code block
    'sphinxcontrib.bibtex', # bibtex style citation
    # 'sphinx_toolbox.collapse',  # collapsable section
    'sphinx_design',     # remplace sphinx_toolbox.collapse
    ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']


# bibliography files
bibtex_bibfiles = ['../../references.bib']