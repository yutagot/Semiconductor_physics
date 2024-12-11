# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Semicondutor physics'
copyright = '2024, Y.G'
author = 'Y.G'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_css_files = ['header.css', 'table.css',  'custom.css']
# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
    \usepackage{amsmath}
    \usepackage{amssymb}
    \usepackage{graphicx}
    ''',
}

master_doc = 'index'
latex_documents = [
    (master_doc, 'SemiconductorPhysics.tex', 'Semiconductor Physics Documentation',
     'Y.G', 'manual'),
]

latex_elements = {
    'preamble': r'''
    % 数式番号を右側に配置
    \usepackage{amsmath}
    \usepackage{etoolbox}
    \numberwithin{equation}{section}
    \makeatletter
    \patchcmd{\@eqnnum}{\hbox}{\hbox to\displaywidth{\hfill} \hbox}{}{}
    \makeatother
    '''
}

