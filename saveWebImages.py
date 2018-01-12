#!/usr/bin/python
# encoding: utf-8
__author__ = 'l'

import urllib
import urllib2
import re
import os


class Spider:
    def __init__(self):
        self.url = 'http://www.2016mq.com/tupianqu/taotu/'
        self.dirName = 'default'
        self.imaDir1 = 'images/'
        if not os.path.exists(self.imaDir1):
            os.mkdir(self.imaDir1)
        else:
            print "Dir Images is exists"

    def getPage(self):
        url = self.url
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode("utf-8")

    def getContents(self):
        page = self.getPage()
        pattern = re.compile(r'http.*?jpg', re.I)
        items = re.findall(pattern, page)
        title = re.findall(r'<title>.*?</title>', page)
        str_title = title[0][7:-8]
        # print str_title
        self.dirName = str_title
        # print items
        # <img src='http://cache3.onlyimg.com/pics/2016120715/457278.jpg'>
        images_url = []
        for item in items:
            # print item
            imagesname = item.split('/')[5]
            # print imagesname
            images_url.append([item, imagesname])
        # print images_url
        return images_url

    def mkDir(self):
        path = self.imaDir1 + self.dirName
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print "path :%s is exists" % path

    def downloadIamegs(self):
        contents = self.getContents()
        self.mkDir()
        for content in contents:
            url = content[0]
            name = content[1]
            urllib.urlretrieve(url, self.imaDir1 + self.dirName + r'/' + name)


spider = Spider()
# spider.getContents()
# spider.mkDir()
spider.downloadIamegs()
