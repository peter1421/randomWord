from flask import Flask, request, render_template
import D
import random
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_data")
def index_add_data():
    try:
        data = [request.args.get("adj", ""),request.args.get("n", ""), request.args.get(
            "p", ""), request.args.get("v", "")]
        op=1
        print("正在輸入",data)
        for x in range(3):
            if(data[x]==''):
                op=0
                print("NULL")
                break
        if(op==1):
            print("資料正在存入資料庫")
            t = D.DataBase()
            t.insert(data[0],data[1],data[2],data[3])
            a = D.DataBase()
            a.Ndelete()
            return render_template("add_data.html", data=data)
    except:
        data="fuck"
    return render_template("erro.html")


@app.route("/show_data")
def index_show_data():
    t = D.DataBase()
    AllData = t.show_all()
    print(AllData)
    ls=[]
    for x in range(4):
        ls.append(random.randint(0, len(AllData)-1))
    print(ls)
    return render_template("data_show.html",data=AllData,ls=ls)

if __name__=="__main__":
    app.run(port=3000,debug=True)


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


