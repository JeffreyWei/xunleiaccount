# -*- coding:utf-8 -*-

__author__ = 'wei'
import random
import time


def removeChineseChar(text):
	text = text.decode('utf-8')
	line = u''
	for char in text:
		if ord(char) >= 256:
			line += " "
		else:
			line += char
	return line


def showData(data):
	random.shuffle(data)
	for line in data:
		if (len(line) < 50):
			print(line)


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
