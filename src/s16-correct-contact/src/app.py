from flask import Flask, request

app = Flask(__name__)


def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content


@app.route("/")
def home():
    return get_html("templates/index")


@app.route("/result")
def result():
    message = request.args.get("message")
    return message
