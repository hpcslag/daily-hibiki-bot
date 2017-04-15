# -*- coding: utf-8 -*-
import requests
import time
from requests.auth import HTTPDigestAuth
import re

def search_article_by_date(date):
	post_url = "https://forum.gamer.com.tw/listtype.php?bsn=60076&subbsn=0&sval=每日響&stype=1"

	headers = {
		'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
		"Content-Type": "application/x-www-form-urlencoded; charset:UTF-8" 
	}

	s = requests.Session()
	r = s.get(post_url,headers=headers)
	origin = r.text.encode('utf-8')

	#filter 1
	regex = r"<a data-gtm=\"B頁文章列表\"(.*?)</a>"
	posts = re.findall(regex, origin,re.M|re.I)

	#filter 2
	find_str = None
	for post in posts:
		regex = r"【艦隊】" + date
		if re.search(regex, post):
			find_str = post

	#filter 3
	if find_str is not None:
		regex = "href=\"//(.*?)\""
		link = "https://" + re.search(regex, find_str,re.M|re.I).group(1)
		return link
	else:
		return None


__all__ = ['search_article_by_date']
#print search_article_by_date("1/5")




