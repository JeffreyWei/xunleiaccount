#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wei'

import urllib2
import utils
from bs4 import BeautifulSoup

def getXunLeiAccount():
	data = []
	url = "http://xlfans.com"
	html = getPage(url)
	soup = BeautifulSoup(html, 'html.parser')

	tag_as = soup.find_all("article", class_="excerpt")
	html =""
	for title in tag_as:
		if utils.checkLink(title.get_text())>=0:
			html = getPage(title.find_all("a")[0].get('href'))
			break
	soup = BeautifulSoup(html, 'html.parser')
	tag_p = soup.find_all("p")
	for line in tag_p:
		text = line.get_text().encode('utf-8')
		# print(line)
		if (text.find("迅雷") >= 0 and text.find("密") >= 0):
			dataList = utils.removeChineseChar(text).split(u'\n')
			for _data in dataList:
				if (len(_data.replace(' ', '')) >= 10):
					data.append(_data)
	return data


def getPage(url):
	'''下载文件html代码，找出一楼的核心代码'''
	opener = urllib2.build_opener()
	# 不加头信息则出现403错误和乱码
	opener.addheaders = [('User-agent', 'Mozilla/5.0')];
	htmlAll = opener.open(url).read()
	# 文件保存编码和文件编辑编码都是utf-8，所以decode一次，不然会出现乱码，但是不影响结果。
	return htmlAll


if __name__ == '__main__':
	data = getXunLeiAccount()
	utils.showData(data)
