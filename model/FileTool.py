#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   FileTool.py    
@Contact :   80491636@qq.com
@Modify Time :   2020/7/11 17:12 
--------------------------------------
'''
import os
import subprocess

from PyQt5.QtCore import pyqtSignal, QThread
from model.upload_video import main, setProxy

"""
搜索当前文件夹
"""


class search(QThread):
    trigger = pyqtSignal(list)

    def __init__(self, path=None):
        super(search, self).__init__()
        if path == None:
            self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#os.path.abspath(os.path.dirname(__file__))
        else:
            self.path = path
        print("搜索当前路径：", self.path)

    def run(self):
        '''

        :return: list MP4文件列表
        '''
        datas = []
        for root, dirs, files in os.walk(self.path):
            print("root", root, 'dirs:', dirs, "files", files)
            for file in files:
                print("file", file)
                #  Python upper() 方法将字符串中的小写字母转为大写字母。
                if file.split('.')[-1].upper() == 'MP4' and file[0] != '.':
                    datas.append(file)
        self.trigger.emit(datas)


"""
上传文件
"""


class upload(QThread):

    def __init__(self,_file_name,_data):
        super(upload, self).__init__()
        self.file_name = _file_name
        self.data = _data

    def run(self):
        # print("房间号：", data[2], "主播名字：", data[4], "是否上传：", data[8])
        playname = self.data[4]
        data_room = self.data[2]
        title = "Music dance"
        description = '▷Live streaming platforms are bursting with dance videos.\n' \
                      '▷各大直播平台劲爆热舞视频。\n' \
                      '▷The video has been reedited！FHD！\n' \
                      '▷视频经过二次编辑，全高清！\n' \
                      '▷You can also leave a like and share my videos if you want !\n' \
                      '▷如果你愿意，也可以点赞，分享我的视频!\n' \
                      '▷Please subscribe for more videos\n' \
                      '▷请订阅我们的频道观看更多视频\n\n' \
                      'Chinese Name：#%s\n' \
                      'Huya TV  ID：%s\n' \
                      '***No Instagram Facebook Twitter*** \n\n' \
                      '➤Donate to my Channel\n' \
                      'https://streamlabs.com/musicdance1\n' \
                      '➤Thanks :) \n\n' \
                      '▷DO not re-upload(must post original link)\n' \
                      '▷请勿直接搬运，转载注明出处！' \
                      % (playname, data_room)
        category = "10"
        keywords = 'Explosive dance,Hd beauty,性感舞蹈,紧身皮裤,皮裤,性感美女,直播舞蹈,丝袜，诱惑'
        t = '--file %s --title %s --description %s --category %d --keywords %s' % (self.file_name, title, description, 10, keywords)
        print(t)
        setProxy()
        main(self.file_name,title,description,category,keywords)


"""
自动上传
"""


class autoup(QThread):

    def __init__(self):
        pass

    def run(self):
        pass
