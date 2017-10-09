__author__ = 'bloodchilde'


import  urllib
import urllib2
import  re
import os
import time

class Spider:
    def __init__(self):
        self.siteUrl="http://sc.chinaz.com/biaoqing/"
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
        self.headers = { 'User-Agent' : self.user_agent }

    def getPage(self,pageIndex):
        url = self.siteUrl+"index_"+str(pageIndex)+".html"
        print url
        request = urllib2.Request(url,headers = self.headers)
        response = urllib2.urlopen(request)
        return response.read().decode("utf-8")

    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)

        pattern = re.compile('''<div.*?class='num_1'.*?>.*?<p>.*?<a.*?href='.*?'.*?target='_blank'.*?title='(.*?)'.*?><img.*?src2="(.*?)".*?>.*?</a>.*?</p>.*?</div>''',re.S)

        items = re.findall(pattern,page)
        print items

        contents=[]

        for item in items:
            print "%s---%s"%(item[0],item[1])
            time.sleep(0.1)
            contents.append([item[0],item[1]])
        return contents

    def mk_dir(self,path):


        isExisist = os.path.exists(path)

        if not isExisist:
            os.makedirs(path)
            return True
        else:
            return False

    def downImage(self,url,dirname):
        imageUrl = url
        request = urllib2.Request(imageUrl,headers = self.headers)
        response = urllib2.urlopen(request)
        imageContents = response.read()

        urlArr = imageUrl.split(u"/")
        imageName = str(urlArr[len(urlArr)-1])

        print imageName

        path = u"C:/l/python/code_python/images"+dirname

        self.mk_dir(path)

        imagePath = path+u"/"+imageName

        f = open(imagePath, 'wb')
        f.write(imageContents)
        f.close()

    def downLoadAllPicture(self,PageIndex):
        contents = self.getContents(PageIndex)

        for list in contents:
            dirname = list[0]
            imageUrl = list[1]
            self.downImage(imageUrl,dirname)




demo = Spider()

for page in range(3,4):
    # demo.downLoadAllPicture(page)
    demo.getContents(page)
