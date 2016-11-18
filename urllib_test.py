#coding: UTF-8 

import urllib,re


def get_content(url):
	'''doc'''
	html = urllib.urlopen(url)
	content = html.read()
	#information = html.info() 
	#code = html.getcode()
	#use_url = html.geturl()  
	#download 
	#urllib.urlretrieve(url,"F:\\163.txt")
	html.close() 
	return(content) 

def get_image(info,num):
	''' get image from info
	<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=6e552df9a3ec08fa260013af69ef3d4d/9c74252dd42a2834adcdbf4d58b5c9ea15cebf3f.jpg" pic_ext="jpeg" width="528" height="297">
	
	<a href="/p/3446756696?pn=2">2</a>
	'''
	regex = r'class="BDE_Image" src="(.+?\.jpg)"'
	pat = re.compile(regex)
	image_code = re.findall(pat,info)
	i = num  
	for image in image_code:
		urllib.urlretrieve(image,"img/%s.jpg"%i)
		i += 1
	return i
		

def next_html(info,urllist):
	url_head = "http://tieba.baidu.com"
	reg = r'a href="(.+?pn\=[0-9])"'
	p = re.compile(reg)
	all_html = re.findall(p,info)
	new_html =[] 
	for html in all_html:
		if html not in new_html:
			new_html.append(url_head+html)
	for item in new_html:
		if item not in urllist:
			urllist.append(item)
	result = urllist
	return(result)
	
'''
def list_add(urllist,url):
	if url is not urllist:
		urllist.append(url)
	return urllist 
'''	
	

urllist = ["http://tieba.baidu.com/p/3446756696/p/3446756696?pn=1"]
num = 1
times = 1
for per_url in urllist:	
	per_info = get_content(per_url)
	urllist = next_html(per_info,urllist)
	new_num = get_image(per_info,num)
	num = new_num
	pri = "第%s页 完成  骚年！"%times
	times += 1
	print pri.encode("gbk")
#print(urllist)

