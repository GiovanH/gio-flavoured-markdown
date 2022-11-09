from flask import Flask
from flask import render_template
from flask import request
import markdown
import customblocks

app = Flask(__name__)
# mde = Mde(app)

md = markdown.Markdown(extensions=["customblocks"])


@app.route("/")
def home():
  markdowncontent = "Hello! I'm *formatted*."
  rendered = md.convert(markdowncontent)
  return render_template("index.html", **locals())

if __name__ == "__main__":
  app.run()
