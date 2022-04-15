import pymysql
import os
import psycopg2
import configparser

class DataBase():
    def __init__(self):
        # self.DATABASE_URL = os.environ['DATABASE_URL']
        # self.DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a web-random-word').read()[:-1]
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            self.DATABASE_URL=config.get('DataBase', 'DATABASE_URL')
            print("連線至:"+self.DATABASE_URL)
            self.db = psycopg2.connect(self.DATABASE_URL, sslmode='require')
            print("連線成功")
        except Exception as e:
                print("連線失敗:"+e)

    # def fetchC(self, query):
    #     cur = self.db.cursor()
    #     cur.execute(query)
    #     table = cur.fetch()
    #     printf(table)
    #     return table

    def fetchAll(self, query):
        cur = self.db.cursor()
        cur.execute(query)
        table = cur.fetchall()
        # for row in table:
        #     print(row[1])
        return table

    def executeQuery(self, query):
        cur = self.db.cursor()
        cur.execute(query)
        print("執行成功")
        self.db.commit()
    # def Ndelete(self):
    #     cur = self.db.cursor()
    #     str = "DELETE FROM wordtable WHERE (noun, place) IN(SELECT noun, place FROM wordtable GROUP BY noun, place HAVING COUNT(*) > 1)"
    #     cur.execute(str)
    #     print("重複值刪除成功")
    #     self.db.commit()

    def close(self, do):
        self.db.cursor().execute(do)
        self.db.commit()


def showQuery(query):
    print("showQuery:{}".format(query))
    print(str)


def getTable(tableName):
    query = "SELECT * FROM {}".format(tableName)
    showQuery(query)
    return query


def getTableCount(tableName):
    query = "SELECT COUNT(*) FROM {}".format(tableName)
    showQuery(query)
    return query


def addData(tableName, word):
    query = "INSERT INTO {} (word) VALUES('{}')".format(tableName, word)
    showQuery(query)
    return query


def deleteData(tableName, word):
    query = "DELETE FROM {} WHERE word = '{}'".format(tableName, word)
    showQuery(query)
    return query


tableName = ["noun", "adjective", "verb", "place"]


def upData(table, word):
    newWord = word+"的"
    query = "UPDATE {} SET word = '{}' WHERE word = '{}'".format(
        table, newWord, word)
    showQuery(query)
    return query


def checkData():
    t = DataBase()
    table = t.fetchAll(getTable(tableName[1]))
    for word in table:
        if("的" not in word[1]):
            try:
                query = upData(tableName[1], word[1])
                t.executeQuery(query)
            except Exception as e:
                print(e)
# checkData()
# # #t.creat_table()
# t = DataBase()

# a=t.fetchAll(getTable(tableName[0]))
# print(a)

# for row in a:
#     print(row)
# a=t.fetchAll(getTableCount(tableName[0]))
# print(a[0])
# t.executeQuery(addData(tableName[1], "熱情的"))
# t.fetchAll(getTable(tableName[0]))

# a=t.show_all()

# # t.insert('難過的','小明','房間','吃飯')
# a=t.show_all()
# print(a)
# print
# t = DataBase()
# t.Ndelete()
# t.insert('d','dd','ddd')
# t.delete(3)
# t.show_all()
