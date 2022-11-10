import logging
import traceback
from flask import Flask
from flask import render_template
from flask import request
import lzstring
import base64

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

with open("static/default_input.md", "r") as fp:
  DEFAULT_INPUT = fp.read()

@app.route('/', methods=['GET'])
def home():
  return render_template("index.html", default_input=DEFAULT_INPUT)

value_arg = "Global"

@app.route('/render')
def render():
  default_value = ""
  
  args = request.args
  value_arg = args.get("q", default_value)
  logging.error(value_arg)
  decoded = base64.b64decode(value_arg).decode("utf-8")
  logging.error(decoded)
  input_str = lzstring.LZString().decompress(str(decoded))
  logging.error(input_str)
  md_html = md.convert(input_str)
  
  return render_template("markdown.html", **locals())

@app.errorhandler(500)
def internal_error(exception):
    print("500 error caught")
    return traceback.format_exc()
  
@app.errorhandler(400)
def internal_error(exception):
    print("400 error caught")
    return traceback.format_exc()
  
if __name__ == "__main__":
  app.run()

  