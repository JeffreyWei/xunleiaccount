#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wei'

import urllib2

from bs4 import BeautifulSoup

def getVIP(webSite):
	url = "http://www.vipfenxiang.com/"+webSite+"/"
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)
	tag_article = soup.find_all('article')[0].find_all('a')[0]
	pageURL = tag_article.get('href')
	html = urllib2.urlopen(pageURL).read()
	soup = BeautifulSoup(html)
	tag_span = soup.find_all("span", attrs={"style": "color: #339966;"})
	for content in tag_span:
		title = content.get_text().encode('UTF-8')
		print(title)

if __name__ == '__main__':
	print("==========优酷==========")
	getVIP("youku")
	print("==========爱奇艺==========")
	getVIP("aiqiyi")
