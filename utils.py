# -*- coding:utf-8 -*-

__author__ = 'wei'
import random

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
		print(line)
