#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wei'

import urllib2
import time
import re
from bs4 import BeautifulSoup


def getXunLeiAccount():
    url = "http://521xunlei.com/portal.php"
    res = urllib2.urlopen(url)
    html = unicode(res.read(), 'GBK').encode('UTF-8')
    soup = BeautifulSoup(html)
    tag_a = soup.find(id="portal_block_62_content").find_all('a')
    for link in tag_a:
        if (checkLink(link.get("title")) >= 0):
            pageURL = "http://521xunlei.com/" + link.get('href')
            html = urllib2.urlopen(pageURL).read()
            soup = BeautifulSoup(html)
            content = soup.find_all("td", class_="t_f")[0]
            flag = "迅雷"
            for text in content.get_text().split("\r\n"):
                text = text.encode('utf-8')
                if (text.find("\n")):
                    text = text.split("\n")[0]
                if (text.find(flag) >= 0):
                    # pat      =   u"([\u4e00-\u9fff]+)"
                    # pattern =   re.compile(pat)
                    # results =   pattern.findall(text)
                    # # 移除中文
                    # for result in results:
                    #     print(result)
                    #     # text=text.replace(result,'\t\t')
                    print(text)
            break


def checkLink(title):
    if title == None:
        return -1
    now = time.localtime(time.time())
    # 会出现标题没有月份的主题
    # date = str(now.tm_mon) + "月" + str(now.tm_mday) + "日"
    date = str(now.tm_mday) + "日"
    title = title.encode('utf-8')
    return title.find(date);


if __name__ == '__main__':
    getXunLeiAccount()




