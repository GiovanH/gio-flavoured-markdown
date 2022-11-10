from flask import Flask
from flask import render_template
from flask import request

import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite

import customblocks

with open('static/markdown.css', "r") as fp:
    md_css = fp.read()

app = Flask(__name__)
# mde = Mde(app)

md = markdown.Markdown(extensions=[
  'fenced_code', 'codehilite', 'tables',
  "customblocks"
])

@app.route('/', methods=['GET'])
def home():
  return render_template("index.html", **locals())


@app.route('/render')
def render():
  default_value = "Hello! I'm *formatted*."
  
  args = request.args
  input_str = args.get("q", default_value)
  
  md_html = md.convert(input_str)
  md_css_html = "<style>{}</style>".format(md_css)

  return md_html + md_css_html

@app.errorhandler(500)
def internal_error(exception):
    print("500 error caught")
    return traceback.format_exc()
  
if __name__ == "__main__":
  app.run()

  