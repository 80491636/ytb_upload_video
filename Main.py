#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Main.py    
@Contact :   80491636@qq.com
@Modify Time :   2020/7/11 16:38 
--------------------------------------
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from mainwindow import Ui_MainWindow
from model.FileTool import search, upload, autoup
from model.SQLSer import SqlSer

class mywindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.sql = SqlSer()

    def searchClick(self):
        '''
        搜索文件夹
        :return:
        '''
        self.search = search()
        self.search.start()
        self.search.trigger.connect(self.searchEnd)
        self.label_info.setText("搜索文件结束")

    def uploadClick(self):
        '''
        上传视频
        :return:
        '''
        file_name,n = self.listwidClick()
        self.upload = upload(file_name,self.datas[n])
        self.upload.start()
        self.label_info.setText("上传文件结束")

    def autoupClick(self):
        '''
        自动上传
        :return:
        '''
        self.label_info.setText("自动上传结束")

    def searchEnd(self, _files):
        '''
        搜索结束
        :return:
        '''
        self.datas = []
        print("搜索到的MP4文件列表：", _files)
        for file in _files:
            print("文件：", file)
            data = self.sql.inquireData(file)
            self.datas.append(data)
            if data[8] == 1:
                self.listWidget.addItem(file + "    已上传" )
            else:
                self.listWidget.addItem(file + "    未上传")
            self.listWidget.setCurrentRow(0)

    def listwidClick(self):
        n = self.listWidget.currentRow()
        t = self.listWidget.item(n).text()
        t = t.split()[0]
        print(t, n)
        return t, n


if __name__ == "__main__":
    # 启动窗口
    app = QApplication(sys.argv)
    MainWindow = mywindow()
    MainWindow.btn_search.clicked.connect(MainWindow.searchClick)
    MainWindow.btn_upload.clicked.connect(MainWindow.uploadClick)
    MainWindow.btn_autoup.clicked.connect(MainWindow.autoupClick)
    MainWindow.listWidget.clicked.connect(MainWindow.listwidClick)
    MainWindow.setWindowTitle('youtube自动上传视频1.0')
    MainWindow.show()
    sys.exit(app.exec_())
