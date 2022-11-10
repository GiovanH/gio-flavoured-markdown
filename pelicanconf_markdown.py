# Import local plugins
import os.path
import sys
import logging

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "markdown-plugins"))

MARKDOWN = {
    'extension_configs': {
        # Utility and enhancement
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.attr_list': {},
        # Extra tags
        'markdown.extensions.toc': {'permalink': "🔗"},
        'markdown.extensions.smarty': {
            'smart_angled_quotes': False,
            'smart_dashes': True,
            'smart_quotes': True,
            'smart_ellipses': True
        },
        # 'pymdownx.tasklist': {},
        'pymdownx.snippets': {
            'check_paths': True,
            'base_path': ['content', '.']
        },
        'pymdownx.tabbed': {},
        'pymdownx.superfences': {
            'preserve_tabs': True,
        },
        'pymdownx.highlight': {
            'extend_pygments_lang': [
                {"name": "php-inline", "lang": "php", "options": {"startinline": True}},
                {"name": "renpy", "lang": "python"}
            ],
            'linenums': 1
        },
        'customblocks': {
            'generators': {}
        },
        "html5video": {},
        "youtube": {},
        # 'spoilerbox': {},
        'mdx_outline': {},
    },
    'output_format': 'html5'
}

from pymdownx.superfences import _escape

def mdx_mermaid_pre(source, language, css_class, options, md, classes=None, id_value='', **kwargs):
    """Format source as code blocks."""

    id_value = ' id="{}"'.format(id_value) if id_value else id_value
    classes = css_class if classes is None else ' '.join(classes + [css_class])

    return f'<div class="mermaid-wrapper"><pre{id_value} class="mermaid {classes}">{_escape(source)}</pre></div>'

def mdx_markdeep(source, language, css_class, options, md, classes=None, id_value='', **kwargs):
    """Format source as code blocks."""

    id_value = ' id="{}"'.format(id_value) if id_value else id_value
    classes = css_class if classes is None else ' '.join(classes + [css_class])

    return f'<div class="mermaid-wrapper"><pre{id_value} class="markdeep {classes}">{_escape(source)}</pre></div>'

def mdx_inlinemarkdeep(source, language, css_class, options, md, classes=None, id_value='', **kwargs):
    """Format source as code blocks."""

    id_value = ' id="{}"'.format(id_value) if id_value else id_value
    classes = css_class if classes is None else ' '.join(classes + [css_class])

    return f'<pre{id_value} class="markdeep {classes}">{_escape(source)}</pre>'

MARKDOWN['extension_configs']['pymdownx.superfences']['custom_fences'] = [
    {
        'name': 'mermaid',
        'class': 'mermaid',
        'format': mdx_mermaid_pre
    },
    {
        'name': 'markdeep',
        'class': 'markdeep',
        'format': mdx_markdeep
    },
    {
        'name': 'inlinemarkdeep',
        'class': 'inlinemarkdeep',
        'format': mdx_inlinemarkdeep
    }
]