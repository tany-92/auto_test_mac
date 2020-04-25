#coding: utf-8
import pymysql.cursors
import json

class OperationSql:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='1992tanyang',
            db='TANYANGTEST',
            charset='utf8',
            #设置返回数据类型
            cursorclass = pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def search_one(self,mysql):
        self.cur.execute(mysql)
        result = self.cur.fetchone()
        return result


if __name__ == '__main__':
    op_mysql = OperationSql()
    res = op_mysql.search_one('select * from user_test where id =1')
    print(res)
    print(type(res))
