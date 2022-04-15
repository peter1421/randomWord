from flask import Flask, request, render_template, redirect, url_for
import D
import database
import random
import json
tableName = ["noun", "adjective", "verb", "place"]


def check(word):
    long = int(len(word))
    print(long)
    if(long <= 0 or long > 10 or word == ' '):
        return False
    else:
        return True


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/getAllData")
def getAllData():
    t = database.DataBase()
    data = {}
    for name in tableName:
        data[name] = t.fetchAll(database.getTable(name))
    print(data)
    return data

@app.route("/addData/<wordType>", methods=['POST'])
def addData(wordType):
    try:
        word = request.form.get(wordType)
        print("input:{}".format(word))
        if(check(word) == False):
            return render_template("erro.html", data="請確認輸入資料")
        t = database.DataBase()
        t.executeQuery(database.addData(wordType, word))
        return redirect("/")
    except Exception as e:
        data = "錯誤原因:{}".format(str(e))
        return render_template("erro.html", data=data)


@app.route("/showData/<wordType>")
def showDataNoun(wordType):
    labels = ["ID", "名詞"]
    t = database.DataBase()
    data = t.fetchAll(database.getTable(wordType))
    print(data)
    return render_template("table.html", title=wordType, labels=labels, data=data)


@app.route("/show_data")
def index_show_data():
    t = D.DataBase()
    AllData = t.show_all()
    print(AllData)
    ls = []
    for x in range(4):
        ls.append(random.randint(0, len(AllData)-1))
    print(ls)
    return render_template("data_show.html", data=AllData, ls=ls)


if __name__ == "__main__":
    app.run(port=30331, debug=True)

