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


@app.route("/addData/adjective", methods=['POST'])
def addData1():
    try:
        name = "adjective"
        word = request.form.get(name)
        print("input:{}".format(word))
        if(check(word) == False):
            return render_template("erro.html", data="請確認輸入資料")
        t = database.DataBase()
        t.executeQuery(database.addData(name, word))
        return redirect("/")
    except Exception as e:
        data = "錯誤原因:{}".format(str(e))
        return render_template("erro.html", data=data)
# 待重構


@app.route("/addData/noun", methods=['POST'])
def addData2():
    try:
        name = "noun"
        word = request.form.get(name)
        if(check(word) == False):
            return render_template("erro.html", data="請確認輸入資料")
        print("input:{}".format(word))
        t = database.DataBase()
        t.executeQuery(database.addData(name, word))
        return redirect("/")
    except Exception as e:
        data = "錯誤原因:{}".format(str(e))
        return render_template("erro.html", data=data)
# 待重構


@app.route("/addData/verb", methods=['POST'])
def addData3():
    try:
        name = "verb"
        word = request.form.get(name)
        if(check(word) == False):
            return render_template("erro.html", data="請確認輸入資料")
        print("input:{}".format(word))
        t = database.DataBase()
        t.executeQuery(database.addData(name, word))
        return redirect("/")
    except Exception as e:
        data = "錯誤原因:{}".format(str(e))
        return render_template("erro.html", data=data)
# 待重構


@app.route("/addData/place", methods=['POST'])
def addData4():
    try:
        name = "place"
        word = request.form.get(name)
        if(check(word) == False):
            return render_template("erro.html", data="請確認輸入資料")
        print("input:{}".format(word))
        t = database.DataBase()
        t.executeQuery(database.addData(name, word))
        return redirect("/")
    except Exception as e:
        data = "錯誤原因:{}".format(str(e))
        return render_template("erro.html", data=data)


@app.route("/showData/noun")
def showDataNoun():
    name = "noun"
    labels = ["ID", "名詞"]
    t = database.DataBase()
    data = t.fetchAll(database.getTable(name))
    print(data)
    return render_template("table.html", title=name, labels=labels, data=data)


@app.route("/showData/adjective")
def showDataAdjective():
    name = "adjective"
    labels = ["ID", "形容詞"]
    t = database.DataBase()
    data = t.fetchAll(database.getTable(name))
    print(data)
    return render_template("table.html", title=name, labels=labels, data=data)


@app.route("/showData/verb")
def showDataVerb():
    name = "verb"
    labels = ["ID", "動詞"]
    t = database.DataBase()
    data = t.fetchAll(database.getTable(name))
    print(data)
    return render_template("table.html", title=name, labels=labels, data=data)


@app.route("/showData/place")
def showDataPlace():
    name = "place"
    labels = ["ID", "地點"]
    t = database.DataBase()
    data = t.fetchAll(database.getTable(name))
    print(data)
    return render_template("table.html", title=name, labels=labels, data=data)


# @app.route("/add_data")
# def index_add_data():
#     try:
#         data = [request.args.get("adj", ""), request.args.get("n", ""), request.args.get(
#             "p", ""), request.args.get("v", "")]
#         op = 1
#         print("正在輸入", data)
#         for x in range(3):
#             if(data[x] == ''):
#                 op = 0
#                 print("NULL")
#                 break
#         if(op == 1):
#             print("資料正在存入資料庫")
#             t = D.DataBase()
#             t.insert(data[0], data[1], data[2], data[3])
#             a = D.DataBase()
#             a.Ndelete()
#             return render_template("add_data.html", data=data)
#     except:
#         data = "fuck"
#     return render_template("erro.html")


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
    app.run(port=3000, debug=True)


# @app.route("/cal")
# def index_c():
#     max = int(request.args.get("max", ""))
#     result = 0
#     for x in range(1, max+1):
#         result += x
#     return render_template("result.html", data=result)


# @app.route("/show")
# def index_s():
#     name = request.args.get("n", "")
#     return "歡迎"+name


# @app.route("/page")
# def index_p():
#     return render_template("page.html")
