import logging
from flask import Flask
from flask import render_template
from flask import request

import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite

import customblocks

import sys
sys.path.append("./peliplugins")
sys.path.append("./mdexts")

import gio_customblocks

with open('static/markdown.css', "r") as fp:
    md_css = fp.read()

app = Flask(__name__)
# mde = Mde(app)

class dummy():
  pass

with open("pelicanconf_markdown.py", "r") as fp:
  exec(fp.read())

pelican_object = dummy()
pelican_object.settings = {
    'MARKDOWN': MARKDOWN
}

gio_customblocks.pelican_init(pelican_object)

md = markdown.Markdown(
  extensions=list(pelican_object.settings['MARKDOWN']['extension_configs'].keys()),
  extension_configs=pelican_object.settings['MARKDOWN']['extension_configs']
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

  