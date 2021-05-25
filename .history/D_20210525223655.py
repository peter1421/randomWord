import pymysql
import os
import psycopg2


class DataBase():
    def __init__(self):
        #self.DATABASE_URL = os.environ['DATABASE_URL']
        self.DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a web-random-word').read()[:-1]
        self.db = psycopg2.connect(self.DATABASE_URL, sslmode='require')
        #self.db = pymysql.connect(host="127.0.0.1", user="fil12385ki", passwd="peter1421", db="fil12385ki",charset="utf8")

    def creat_table(self):
        create_table_query = '''CREATE TABLE wordtable(
            adjective varchar(10),
            noun varchar(10),
            place varchar(10),
            verb varchar(10));'''
        self.close(create_table_query)
        print("列表已建立")

    def show_all(self):
        print("show:")
        cur = self.db.cursor()
        cur.execute("SELECT * FROM wordtable")
        table = cur.fetchall()
        for row in cur.fetchall():
            print(row)
        return table

    def insert(self, v_a, v_n, v_p, v_v):
        cur = self.db.cursor()
        str = "INSERT INTO wordtable(adjective, noun, place, verb) VALUES('{}', '{}', '{}', '{}')".format(
            v_a, v_n, v_p, v_v)
        cur.execute(str)
        
        
        print("添加成功")

    def delete(self, num):
        cur = self.db.cursor()
        str = "DELETE FROM wordtable WHERE id = {}".format(num)
        cur.execute(str)

    def close(self, do):
        self.db.cursor().execute(do)
        self.db.commit()
t = DataBase()
#t.creat_table()
#t.insert('難過的','小明','房間','吃飯')
a=t.show_all()
print(a)
# print

# t.insert('d','dd','ddd')
# t.delete(3)
# t.show_all()
