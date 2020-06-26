import json
import re
import bs4
import os
import time
import requests
start_time = time.time()
links_handle=open('mobiles_total.json','r')
links=json.loads(links_handle.read())
x=0
# length=len(links['samsung'])
for brand in links:
	if brand!='samsung':
		os.mkdir(f'html/{brand}')
		for i,link in enumerate(links[brand]):
			html=requests.get(link)
			file_name=link.replace('https://mobizil.com/','').replace('/','')
			# soup = bs4.BeautifulSoup(html.text,'lxml')
			html_handle=open(f'html/{brand}/{file_name}.html','w+')	
			html_handle.write(html.text)
			html_handle.close()
			x=x+1
			print(x)
end_time = time.time()
taken=end_time-start_time
print(f'time taken{taken}s')



