#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SQLSer.py    
@Contact :   80491636@qq.com
@Modify Time :   2020/7/12 21:47 
--------------------------------------
'''

import time

import pymysql
from pymysql import OperationalError


class SqlSer(object):

    def __init__(self):

        # 连接数据库
        self.connect = pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='123456',
            db='huya',
            charset='utf8',
        )

        # 获取游标
        self.cursor = self.connect.cursor()

    def addData(self, datas, filename):
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 插入数据
        sql = "INSERT INTO hyvideo (data_id, data_room, playtime, playname, img, filename, date) VALUES \
        ( '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
        data = (datas['dataid'], datas['roomid'], datas['playtime'], datas['playname'], datas['playimg'], filename, t)
        self.cursor.execute(sql % data)
        self.connect.commit()
        print('成功插入', self.cursor.rowcount, '条数据')

    def inquireData(self, _fileName):
        # 查询数据
        sql = "SELECT * FROM hyvideo WHERE filename = '%s' limit 1"
        data = (_fileName,)
        self.cursor.execute(sql % data)
        data = self.cursor.fetchone()
        print(type(data))
        print("data :", data)
        print("房间号：", data[2], "主播名字：", data[4], "是否上传：", data[8])
        return data

    def upData(self, _id):
        # 修改数据
        sql = "UPDATE hyvideo SET uploadis = %.2f WHERE id = '%.2f' "
        data = (1, _id)
        self.cursor.execute(sql % data)
        self.connect.commit()
        print('成功修改', self.cursor.rowcount, '条数据')

    def closeSer(self):
        # 关闭连接
        self.cursor.close()
        self.connect.close()
