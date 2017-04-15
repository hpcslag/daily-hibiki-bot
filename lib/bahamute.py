# -*- coding: utf-8 -*-
import requests
import time
from requests.auth import HTTPDigestAuth
import re

def get_images_on_article (url):

	post_url = url

	headers = {
		'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
		"Content-Type": "application/x-www-form-urlencoded; charset:UTF-8" 
	}

	s = requests.Session()
	r = s.get(post_url,headers=headers)
	origin = r.text.encode('utf-8')

	#filter 1
	regex = r"<!--文章內文-->((.|\n|\r)*?)<!--文章內文結束-->"
	origin = re.search(regex, origin,re.M|re.I).group(1)

	#filter 2
	regex = r"<a name=\"attachImgName\" href=\"(.*?)\""
	pictures = re.findall(regex, origin,re.M|re.I)

	return pictures

__all__ = ['get_images_on_article']
#print get_images_on_article("https://forum.gamer.com.tw/C.php?bsn=60076&snA=3892195&tnum=44")