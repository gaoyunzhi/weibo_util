#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import weiboo
import time

def testSearch(key):
	# for url, card in weiboo.search(key):
	# 	print(url, weiboo.getCount(card))
	with open('tmp.txt', 'w') as f:
		f.write(str(weiboo.search(key)))

def testSearchUser(key):
	print(weiboo.searchUser(key))
	time.sleep(10)

def backfill(key):
	print(len(weiboo.backfill(key, limit = 4)))

if __name__=='__main__':
	backfill('5402666134')
	# testSearch('6622333936')
	# testSearchUser('澎湃新闻')
	# testSearchUser('5044281310')