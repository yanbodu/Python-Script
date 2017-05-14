# coding:utf-8
# A Python spider to download pictures from www.mzitu.com
# @ Yanbo Du

import requests
from lxml import html
import os
import time


# main page
def getPage(num):
    urls = []

    baseUrl = 'http://www.mzitu.com/page/{}'.format(num)
    selector = html.fromstring(requests.get(baseUrl).content)
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
    jpgList = []
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
def downloadPic(piclist, count):

    for i in piclist:
        # check website status
        if requests.get(i).status_code == 200:
            # currentPath/dir/fielname
            filename = '%s/%s.jpg' % (os.path.abspath('.'), count)
            print (u'Downloading: No.%s' %  count)
            with open(filename, "wb") as jpg:
                jpg.write(requests.get(i).content)
                time.sleep(2)
            count += 1
        else:
            print ('Crash!!')
            return

if __name__ == '__main__':
    # ask user for page number to download
    pageNum = input(u'Page Number: ')

    start =time.clock()

    num = 0
    count = 0
    picture = []
    for num in range(int(pageNum)):
        # save pictures in the list
        for link in getPage(num):
            picture = getPiclink(link)
            # download pictures
            downloadPic(picture, count)
            count = count + len(picture)
        num += 1

    end = time.clock()

    print('Running time: %s Seconds'%(end-start))
