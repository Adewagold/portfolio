from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world_default():
    return render_template("index.html")


@app.route("/index.html")
def hello_world():
    return render_template("index.html")


@app.route("/<string:page_name>")
def hello_world_name(page_name):
    return render_template(page_name)



