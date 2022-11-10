from flask import Flask
from flask import render_template
from flask import request

import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite

import customblocks

import peliplugins


with open('static/markdown.css', "r") as fp:
    md_css = fp.read()

app = Flask(__name__)
# mde = Mde(app)


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

md = markdown.Markdown(
  extensions=[
    'fenced_code', 'codehilite', 'tables',
    'customblocks'
  ],
  extension_configs=MARKDOWN['extension_configs']
)

@app.route('/', methods=['GET'])
def home():
  return render_template("index.html", **locals())


@app.route('/render')
def render():
  default_value = ""
  
  args = request.args
  input_str = args.get("q", default_value)
  
  md_html = md.convert(input_str)
  
  return render_template("markdown.html", **locals())

@app.errorhandler(500)
def internal_error(exception):
    print("500 error caught")
    return traceback.format_exc()
  
if __name__ == "__main__":
  app.run()

  