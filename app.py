from flask import Flask, request, render_template, redirect, url_for, session
import database
import random
import json
import os
from datetime import timedelta

tableName = ["noun", "adjective", "verb", "place"]

app = Flask(__name__, static_folder='static', static_url_path='')
app.config['SECRET_KEY'] = "oiuytrewqasdfghjklmnhytg"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=10)


def check(word):
    try:
        session["addTimes"] = int(session.get('addTimes'))
        print("Add")
    except:
        session["addTimes"] = 0
        print("Init")
    long = int(len(word))
    addTimes = str(session.get('addTimes'))
    print("已添加次數:"+addTimes+"!")
    if(int(addTimes) > 20 or long <= 0 or long > 10 or word == ' ' or '1=1' in word):
        return False
    else:
        return True


@app.route("/")
def index():
    try:
        session["addTimes"] = int(session.get('addTimes'))
        print("Add!!")
    except:
        session["addTimes"] = 0
        print("Init!!")
    return render_template("index.html")


@app.route("/api/getAllData")
def getAllData():
    t = database.DataBase()
    data = {}
    for name in tableName:
        data[name] = t.fetchAll(database.getTable(name))
    # print(data)
    data["addTimes"] =session.get("addTimes")
    return data

# @app.route("/api/getSession/<id>")
# def getSession(id):
#     print("取得ID:",id)
#     data ='{'+'"{}":"{}"'.format(id,session.get(id))+'}'
#     return json.loads(data)

@app.route("/addData/<wordType>", methods=['POST'])
def addData(wordType):
    try:
        word = request.form.get(wordType)
        print("input:{}".format(word))
        if(check(word) == False):
            return render_template("erro.html", data="請確認輸入資料")
        t = database.DataBase()
        t.executeQuery(database.addData(wordType, word))
        session["addTimes"]+=1
        return redirect("/")
    except Exception as e:
        data = "錯誤原因:{}".format(str(e))
        return render_template("erro.html", data=data)


@app.route("/showData/<wordType>")
def showDataNoun(wordType):
    labels = ["ID", wordType]
    t = database.DataBase()
    data = t.fetchAll(database.getTable(wordType))
    print(data)
    return render_template("table.html", title=wordType, labels=labels, data=data)


if __name__ == "__main__":
    app.run(port=30331, debug=True)
