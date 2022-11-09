from flask import Flask
from flask import render_template
from flask import request
import markdown
import customblocks

app = Flask(__name__)
# mde = Mde(app)

md = markdown.Markdown(extensions=["customblocks"])

@app.route('/', methods=['GET'])
def home():
  return render_template("index.html", **locals())


@app.route('/render', methods=['POST'])
def render():
  default_value = "Hello! I'm *formatted*."
  markdowncontent = request.form.get('textarea', default_value)
  rendered = md.convert(markdowncontent)
  return rendered

if __name__ == "__main__":
  app.run()

  