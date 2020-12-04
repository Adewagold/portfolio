from flask import Flask, render_template, url_for, request, redirect
import io
import csv

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


def write_to_file(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    with open("database.txt", "a") as database:
        database.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    header = ["Email", "Subject", "Message"]
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    with open("database.csv", "a") as database2:
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["GET", "POST"])
def submit_form(email=None):
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            return "Cannot save to the database at this time."
    else:
        return "Something went wrong. Try again!"
