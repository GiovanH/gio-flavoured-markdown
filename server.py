import logging
import traceback
from flask import Flask
from flask import render_template
from flask import request
from lzstring import LZString
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

extension_configs = pelican_object.settings['MARKDOWN']['extension_configs']

print(extension_configs)

with open("static/mdtemplate_default.txt", "r") as fp:
  DEFAULT_INPUT = fp.read()

@app.route('/', methods=['GET'])
def home():
  return render_template("index.html", default_input=DEFAULT_INPUT)

value_arg = "Global"

@app.route('/render')
def render():
  default_value = ""

  value_arg = request.args.get("q", default_value)
  input_str = LZString.decompressFromEncodedURIComponent(value_arg) or ''
  md_html = markdown.markdown(
    text=input_str,
    extensions=list(extension_configs.keys()),
    extension_configs=extension_configs
  )
  
  return render_template("markdown.html", **locals())

@app.route('/template/<name>')
def renderMdTemplate(name):
  try:
    with open(f"static/mdtemplate_{name}.txt", "r") as fp:
      return fp.read()
  except:
    return traceback.format_exc()
  
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

  