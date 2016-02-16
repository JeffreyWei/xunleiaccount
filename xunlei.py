#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wei'

import urllib2
import time
import utils
from bs4 import BeautifulSoup
import gzip, cStringIO


def getXunLeiAccount():
	data = []
	html = getPageHTML('http://521xunlei.com/portal.php')
	soup = BeautifulSoup(html, 'html.parser')
	tag_a = soup.find(id="portal_block_62_content").find_all('a')
	for link in tag_a:
		if (checkLink(link.get("title")) >= 0):
			pageURL = "http://521xunlei.com/" + link.get('href')
			html = getPageHTML(pageURL)
			soup = BeautifulSoup(html, 'html.parser')
			content = soup.find_all("td", class_="t_f")[0]
			flag = "迅雷"
			# flag2 = "迅雷会员账号"
			for text in content.get_text().split("\r\n"):
				text = text.encode('utf-8')
				if (text.find("\n")):
					text = text.split("\n")[0]
				if (text.find(flag) >= 0):
					for line in text.split("\n"):
						if (line.find(flag) >= 0 and len(line) < 90):
							_data=utils.removeChineseChar(line)
							if (len(_data.replace(' ',''))>=10):
								data.append(_data)
			break
	return data;


def checkLink(title):
	if title == None:
		return -1
	now = time.localtime(time.time())
	# 会出现标题没有月份的主题
	# date = str(now.tm_mon) + "月" + str(now.tm_mday) + "日"
	# date = str(now.tm_mday) + "日"
	date = str(now.tm_mday)
	title = title.encode('utf-8')
	return title.find(date);


def getPageHTML(url):
	req = urllib2.Request(url);
	req.add_header('Accept-Encoding', 'gzip, deflate');
	f = urllib2.urlopen(req, timeout=30)
	html = f.read()
	# gzip解压缩
	if html[:6] == '\x1f\x8b\x08\x00\x00\x00':
		html = gzip.GzipFile(fileobj=cStringIO.StringIO(html)).read()
	html = html.decode('gbk')
	return html


if __name__ == '__main__':
	data=getXunLeiAccount()
	utils.showData(data)
