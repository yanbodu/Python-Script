# coding:utf-8
# A Python spider to download pictures from www.mzitu.com
# @ Yanbo Du

import requests
from lxml import html
import os
import time

jpgList = []

# main page
def getPage(pageNum):
    baseUrl = 'http://www.mzitu.com/page/{}'.format(pageNum)
    selector = html.fromstring(requests.get(baseUrl).content)
    urls = []
    for i in selector.xpath('//ul[@id="pins"]/li/a/@href'):
        urls.append(i)
    return urls


# save pictures to the list
def getPiclink(url):
    sel = html.fromstring(requests.get(url).content)
    # Total picture number
    total =  sel.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()')[0]
    # Title
    title = sel.xpath('//h2[@class="main-title"]/text()')[0]
    # put url to the list
    for i in range(int(total)):
        # single page
        link = '{}/{}'.format(url, i+1)
        s = html.fromstring(requests.get(link).content)
        # save src attribute
        jpg = s.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
        # put a single picture to the list
        jpgList.append(jpg)
    return jpgList


# download pictures
def downloadPic(piclist):
    k = 1
    # number of Picture
    count = len(piclist)
    # dir Name
    dirName = u"[%sP]%s" % (str(count), 'Pictures')
    # new dir
    os.mkdir(dirName)
    for i in piclist:
        # check website status
        if requests.get(i).status_code == 200:
            # currentPath/dir/fielname
            filename = '%s/%s/%s.jpg' % (os.path.abspath('.'), dirName, k)
            print (u'Downloading:%s No.%s' % (dirName, k))
            with open(filename, "wb") as jpg:
                jpg.write(requests.get(i).content)
                time.sleep(2)
            k += 1
        else:
            print ('Crash!!')
            return

if __name__ == '__main__':
    # ask user for page number to download
    pageNum = input(u'Page Number: ')

    # save pictures in the list
    for link in getPage(pageNum):
        getPiclink(link)

    # download pictures
    downloadPic(jpgList)
