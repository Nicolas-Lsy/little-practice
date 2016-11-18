#coding: UTF-8 
#python3
import urllib.request  
#BeautifulSoup  Ubuntu apt-get install Python-bs4 
from bs4 import BeautifulSoup 

def get_content(url):
	''' get content from url '''
	html = urllib.request.urlopen(url)
	content = html.read() 
	html.close() 
	return content 
	
def get_image(info):
	''' doc '''
	soup = BeautifulSoup(info)
	
	all_img = soup.find_all('img', class_="BDE_Image")
	url_list = [img['src'] for img in all_img]
	
	return(url_list) 
	
def download_img(img_list):
	x = 1
	for img in img_list:
		img_name = '%s.jpg'%x 
		urllib.request.urlretrieve(img,'img/'+img_name)
		x += 1
		print("get " + img_name)
	
url = "http://tieba.baidu.com/p/4308356890"
info = get_content(url)

list = get_image(info)

download_img(list)
