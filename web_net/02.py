#!/usr/bin/python
#Filename:02.py

import urllib2

def getURL(str):
	start = str.find(r'href=')
	start += 6
	end   = str.find(r'.html')
	end   += 5
	url = str[start : end]
	return url

def getContext(url):
	text = urllib2.urlopen(url).read()
	return text

def storeContext(url):
	content = getContext(url)
	filename = url[-20:]
	open("./1.html", 'w').write(content)

if __name__ == '__main__':
	str = '<td class="help"><a href="http://www.baidu.com/search/news_help.html">帮助</a><span class="sep">'
	url = getURL(str)
	storeContext(url)
