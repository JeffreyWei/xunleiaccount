#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wei'

import urllib2
import time
import re
from bs4 import BeautifulSoup


def getXunLeiAccount():
    url = "http://xlfans.com"
    html = getPage(url)
    soup = BeautifulSoup(html)
    tag_a = soup.find_all("article", class_="excerpt")[0]
    html = getPage(tag_a.find_all("a")[0].get('href'))
    soup = BeautifulSoup(html)
    tag_p =soup.find_all("p")
    for line in tag_p:
        text=line.get_text().encode('utf-8')
        if(text.find("迅雷")>=0 and text.find("密码")>=0):
            print(line)

def checkLink(title):
    if title == None:
        return -1
    now = time.localtime(time.time())
    # 会出现标题没有月份的主题
    # date = str(now.tm_mon) + "月" + str(now.tm_mday) + "日"
    date = str(now.tm_mday) + "日"
    title = title.encode('utf-8')
    return title.find(date);

def getPage(url):
    '''下载文件html代码，找出一楼的核心代码'''
    opener = urllib2.build_opener()
    # 不加头信息则出现403错误和乱码
    opener.addheaders = [('User-agent', 'Mozilla/5.0')];
    htmlAll = opener.open(url).read()
    # reg1Floor = '<div class="msgfont">(.*?)</div>'
    # html = re.search(reg1Floor,htmlAll)
    # html = html.group()
    # 文件保存编码和文件编辑编码都是utf-8，所以decode一次，不然会出现乱码，但是不影响结果。
    return htmlAll


if __name__ == '__main__':
    getXunLeiAccount()
