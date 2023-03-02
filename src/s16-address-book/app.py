from flask import Flask

app = Flask(__name__)


def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content


def get_data():
    path = "assets/data.txt"
    with open(path, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        lines.sort()
        lines = [line.strip() for line in lines]
    return lines


@app.route("/")
def home_page():
    return get_html("templates/index")


@app.route("/guests")
def guests_page():
    guests_list = get_html("templates/guests")
    datas = get_data()
    values = ""
    for data in datas:
        values += "<p>" + data + "</p>"
    return guests_list.replace("$$DATA$$", values)
