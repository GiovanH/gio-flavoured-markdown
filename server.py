from flask import Flask
from flask import render_template
from flask import request
# from flask_mde import Mde

app = Flask(__name__)
# mde = Mde(app)

@app.route("/")
def home():
  rendered = "Hello!"
  return render_template("index.html")

if __name__ == "__main__":
  app.run()
