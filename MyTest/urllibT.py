#!/usr/bin/env python
# first time try to use urllib to get web info from some websit
# @time: 2018-7-1 18:44:55
# @author: asange
import urllib.request
import nltk
import firstT

def main():
	url = 'https://www.cnblogs.com/wanghao123/p/7921654.html'
	# open url stream to read info 
	page_info = urllib.request.urlopen(url)
	html = page_info.read().decode(encoding='utf-8', errors='strict')
	# get word from page by nltk
	fdlist = nltk.word_tokenize(html)
	html_dict = {}
	# count word
	for x in fdlist:
		html_dict[x] = (1 if x not in html_dict else html_dict[x]+1)
	print(firstT.sortDict(html_dict))
	# print(html_dict)

if __name__ == '__main__':
	main()