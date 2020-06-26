import json
import bs4
import re
import requests
# url_mobile='http://www.mobizil.com/mobiles'
# mobile_html=requests.get(url_mobile)
# soup = bs4.BeautifulSoup(mobile_html.text,'lxml')

mobile_brand_list=['https://mobizil.com/mobiles/samsung/', 'https://mobizil.com/mobiles/apple/', 'https://mobizil.com/mobiles/huawei/', 'https://mobizil.com/mobiles/oppo/', 'https://mobizil.com/mobiles/xiaomi/', 'https://mobizil.com/mobiles/honor/', 'https://mobizil.com/mobiles/realme/', 'https://mobizil.com/mobiles/infinix/', 'https://mobizil.com/mobiles/nokia/', 'https://mobizil.com/mobiles/vivo/', 'https://mobizil.com/mobiles/sony/', 'https://mobizil.com/mobiles/tecno/', 'https://mobizil.com/mobiles/htc/', 'https://mobizil.com/mobiles/oneplus/', 'https://mobizil.com/mobiles/lg/', 'https://mobizil.com/mobiles/meizu/', 'https://mobizil.com/mobiles/lenovo/', 'https://mobizil.com/mobiles/motorola/', 'https://mobizil.com/mobiles/blackberry/', 'https://mobizil.com/mobiles/microsoft/', 'https://mobizil.com/mobiles/alcatel/', 'https://mobizil.com/mobiles/gionee/', 'https://mobizil.com/mobiles/oneclick/', 'https://mobizil.com/mobiles/zte/', 'https://mobizil.com/mobiles/others/']
# for ultag in soup.find_all('ul', {'class': 'aps-brands-list2'}):
# 	for litag in ultag.find_all('li'):
# 		mobile_source_list.append(litag.a.get('href'))
# 		#litag.img.get('src')

#attribute check
# sample=open('sample.json','r')
# data=json.loads(sample.read())
# products=[product for product in data['products']]
# for i,j in enumerate(products):
# 	for feild in product_feilds:
# 		print(j[feild])



# mobile_links={}
# for each in mobile_brand_list:
# 	z=each.split('/')
# 	mobile_links[z[4]]=[]
# 	each_html=requests.get(each)
# 	soup = bs4.BeautifulSoup(each_html.text,'lxml')
# 	for divtag in soup.find_all('div', {'class': 'aps-product-box'}):
# 		mobile_links[z[4]].append(divtag.a.get('href'))
# print(len(mobile_links))
# write_links=open('mobile_products_links.json','w+')
# write_links.write(json.dumps(mobile_links,indent=4))
# write_links.close()


# merge /new-mobiles with mobiles 
# data_handle=open('mobile_products_links.json','r')
# mobile_links=json.loads(data_handle.read())
# url='https://mobizil.com/new-mobiles'
# new=0
# for i in range(2,39):
# 	url_pages=f'https://mobizil.com/new-mobiles/page/{i}/'
# 	html=requests.get(url_pages)
# 	soup = bs4.BeautifulSoup(html.text,'lxml')
# 	for divtag in soup.find_all('div', {'class': 'aps-product-box'}):
# 		link=divtag.a.get('href')
# 		m=0
# 		if 'iphone' in link:
# 			if link in mobile_links['apple']:
# 				m=1
# 				break
# 			else:
# 				m=1
# 				# print('apple',link)
# 				mobile_links['apple'].append(link)
# 				new=new+1
# 				break
# 		if 'one-click' in link:
# 			if link in mobile_links['oneclick']:
# 				m=1
# 				break
# 			else:
# 				m=1
# 				mobile_links['oneclick'].append(link)
# 				# print('oneclick',link)
# 				new=new+1
# 				break
# 		for brand in mobile_links:
# 			if re.search(brand,link):
# 				if link in mobile_links[brand]:
# 					m=1
# 					pass
# 				else:
# 					m=1
# 					new=new+1
# 					mobile_links[brand].append(link)
# 					# print(brand,link)
# 		if m==0:
# 			if link in mobile_links['others']:
# 				pass
# 			else:
# 				new=new+1
# 				mobile_links['others'].append(link)
# 				# print(link)
# 	# mobile_links[].append(divtag.a.get('href'))
# new_hanle=open('mobiles_total.json','w+')
# new_hanle.write(json.dumps(mobile_links,indent=4))
# new_hanle.close()
# print(new)



