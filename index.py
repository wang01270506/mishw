from flask import Flask,render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1></h1>"
    homepage += "<a href=/mis>我的個人簡介</a><br>"
    homepage += "<a href=/today>MIS相關工作介紹</a><br>"
    homepage += "<a href=/welcome?nick=ting>職涯測驗結果</a><br>"
    homepage += "<a href=/about>求職履歷自傳</a><br>"
    return homepage

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/about")
def about():
    return render_template("aboutme.html")


if __name__ == "__main__":
    app.run()
