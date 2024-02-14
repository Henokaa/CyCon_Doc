# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'CyCon'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'navigation_depth': 4,
    'titles_only': False,
    'collapse_navigation': False,
    'includehidden': True,
    'html_last_updated_fmt': '%b %d, %Y',
    'html_show_sourcelink': False,
    'pages': [
        {
            'page': 'index',
            'title': 'Home',
            'link': 'index.html',
        },
        {
            'page': 'Logistic regression',
            'title': 'Logistic Regression',
            'link': 'logistic-regression.html',
        },
        {
            'page': 'KNN',
            'title': 'KNN',
            'link': 'knn.html',
        },
        {
            'page': 'Perceptron',
            'title': 'Perceptron',
            'link': 'Perceptron.html',
        },
        {
            'page': 'FAQ',
            'title': 'Frequently Asked Questions',
            'link': 'faq.html',
        },
    ],
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
