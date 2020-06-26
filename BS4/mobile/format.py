import json
import os
import re
import bs4
import glob
import numpy as np
cwd=os.getcwd()
products=[]
product_feilds=['title', 'author', 'date', 'date_gmt', 'content', 'status', 'comment_status', 'image', 'gallery', 'meta', 'terms']
# json_handler=open('sample.json','r')
# sample_json=json.loads(json_handler.read())
sample={"aps-attr-group-438": 
			{
				"391": "galaxy s10 lite",
				"392": "s10",
				"393": "01-04-2020",
				"394": " \u0645\u062a\u0627\u062d \u0644\u0644\u0628\u064a\u0639"
			},
			"aps-attr-group-440": {
				"125": "Yes",
				"126": "Yes",
				"127": "Yes",
				"439": "Yes",
				"395": "\u0645\u0645\u062a\u0627\u0632\u0629",
				"396": "sim",
				"397": "Yes"
			},
			"aps-attr-group-441": {
				"398": "161.8x75.8x8.7 \u0645\u0644\u0645",
				"399": "195 \u062c\u0631\u0627\u0645",
				"400": "\u0632\u062c\u0627\u062c",
				"401": "\u0627\u0644\u0627\u0628\u064a\u0636 - \u0627\u0644\u0627\u062e\u0636\u0631",
				"402": "No"
			},
			"aps-attr-group-442": {
				"403": "AMOLED",
				"404": "6.5 \u0628\u0648\u0635\u0629 \u0628\u062f\u0648\u0646 \u0627\u064a \u0646\u0648\u062a\u0634",
				"405": "1080x2340",
				"406": "16 \u0645\u0644\u064a\u0648\u0646 \u0644\u0648\u0646",
				"407": "333",
				"408": "\u062c\u0648\u0631\u064a\u0644\u0627 \u0627\u0644\u062c\u064a\u0644 \u0627\u0644\u062e\u0627\u0645\u0633"
			},
			"aps-attr-group-443": {
				"409": "\u0631\u0628\u0627\u0639\u064a\u0629 \u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629 48 \u0645.\u0628 \u0628\u0641\u062a\u062d\u0629 \u0639\u062f\u0633\u0629 F\/1.7 \u0648\u0627\u0644\u062b\u0627\u0646\u064a\u0629 \u0644\u0644\u062a\u0635\u0648\u064a\u0631 \u0627\u0644\u0648\u0627\u0633\u0639 8 \u0645.\u0628 \u0628\u0641\u062a\u062d\u0629 \u0639\u062f\u0633\u0629 F\/2.2 \u0648\u0627\u0644\u062b\u0627\u0644\u062b\u0629 \u0644\u0644\u0639\u0632\u0644 2 \u0645.\u0628 \u0628\u0641\u062a\u062d\u0629 \u0639\u062f\u0633\u0629 F\/2.4 \u0648\u0627\u0644\u0631\u0627\u0628\u0639\u0629 \u0644\u0644\u0645\u0627\u0643\u0631\u0648 2 \u0645\u064a\u062c\u0627 \u0628\u0643\u0633\u0644 \u0628\u0641\u062a\u062d\u0629 \u0639\u062f\u0633\u0629 F\/2.4",
				"410": "1080p@30fps, 720p@30fps",
				"411": "HDR, panorama",
				"412": "\u0645\u0632\u062f\u0648\u062c LED",
				"413": "16 \u0645\u064a\u062c\u0627 \u0628\u0643\u0633\u0644 \u0641\u062a\u062d\u0629 \u0639\u062f\u0633\u0629 f\/2.0"
			},
			"aps-attr-group-444": {
				"414": "Mediatek Helio P70 \u062b\u0645\u0627\u0646\u064a \u0627\u0644\u0646\u0648\u0627\u0629 \u0628\u062a\u0643\u0646\u0648\u0644\u0648\u062c\u064a\u0627 12 \u0646\u0627\u0646\u0648",
				"415": "Mali-G72 MP3",
				"416": "8 \u062c\u064a\u062c\u0627 \u0631\u0627\u0645",
				"417": "128 \u062c\u064a\u062c\u0627 \u0628\u0627\u064a\u062a",
				"418": "\u064a\u062f\u0639\u0645 \u062d\u062a\u0649 256 \u062c\u064a\u062c\u0627 \u0628\u0627\u064a\u062a \u0641\u064a \u0645\u0646\u0641\u0630 \u0645\u0646\u0641\u0635\u0644 \u0628\u0647",
				"419": "\u0641\u064a \u0627\u0644\u0623\u0645\u0627\u0645\/\u0628\u0627\u0644\u0634\u0627\u0634\u0629",
				"420": "\u0633\u0631\u064a\u0639\u0629",
				"421": "Yes",
				"422": "\u0627\u0644\u0628\u0635\u0645\u0629 \u0645\u062f\u0645\u062c\u0629 \u0628\u0627\u0644\u0634\u0627\u0634\u0629 , \u0627\u0644\u062a\u0633\u0627\u0631\u0639 , \u0627\u0644\u0642\u0631\u0628 , \u0627\u0644\u0628\u0648\u0635\u0644\u0629 , \u0627\u0644\u062c\u064a\u0631\u0648\u0633\u0643\u0648\u0628"
			},
			"aps-attr-group-445": {
				"423": "ANDROID 10",
				"424": "ColorOS 6.1"
			},
			"aps-attr-group-446": {
				"425": "4000",
				"426": "\u063a\u064a\u0631 \u0642\u0627\u0628\u0644\u0629 \u0644\u0644\u0627\u0632\u0627\u0644\u0629",
				"427": "Yes",
				"428": "20 \u0648\u0627\u0637",
				"430": "Yes"
			},
			"aps-attr-group-447": {
				"431": "v4.2",
				"253": "Wi-Fi 802.11 a\/b\/g\/n\/ac, dual-band, Wi-Fi Direct, hotspot",
				"254": "Yes",
				"240": "Type C \u0643\u0645\u0627 \u064a\u062f\u0639\u0645 \u0627\u0644\u0640 OTG",
				"195": "Yes",
				"432": "with A-GPS, GLONASS, BDS",
				"183": "No"
			},
			"aps-attr-group-448": {
				"433": "Mono \/ \u0633\u0645\u0627\u0639\u0629 \u0648\u0627\u062d\u062f\u0629",
				"434": "\u0639\u0627\u0644\u064a",
				"435": "No",
				"436": "\u064a\u062f\u0639\u0645 \u0645\u062f\u062e\u0644 3.5 \u0645\u0645",
				"437": "\u0646\u0639\u0645"
			}
		}

features_names={
'cpu':'\u0627\u0644\u0645\u0639\u0627\u0644\u062c',
'ram':'\u0627\u0644\u062a\u062e\u0632\u064a\u0646 \/ \u0627\u0644\u0631\u0627\u0645',
'camera':'\u0627\u0644\u0643\u0627\u0645\u064a\u0631\u0627',
'display':'\u0627\u0644\u0634\u0627\u0634\u0629',
'gears':'\u0646\u0638\u0627\u0645 \u0627\u0644\u062a\u0634\u063a\u064a\u0644',
'battery':'\u0627\u0644\u0628\u0637\u0627\u0631\u064a\u0629'
}
os.chdir('html/samsung/')
files=glob.glob('*.html')
os.chdir(cwd)
for file in files:
	obj={}
	soup = bs4.BeautifulSoup(open(f'{cwd}/html/samsung/{file}'),'lxml')
	title = soup.select('h1.aps-main-title')[0].text.strip()
	img=soup.select('div.aps-product-pic')[0].img.get('src')
	gallery_links=soup.find_all('img',{'class':'alignnone'})
	obj['gallery']=[ele.get('src') for ele in  gallery_links]
	obj['image']=img
	obj['title']=title
	obj['author']="1"
	obj['date']="2017-02-25 21:05:11"
	obj['date_gmt']= "2017-02-25 16:05:11"
	obj['meta']={}
	randnums= np.random.randint(8,11,10)
	obj['meta']['aps-product-rating']= {
				"design": 9,
				"display": 10,
				"camera": 9,
				"multimedia": 10,
				"features": 9,
				"connectivity": 9,
				"call-quality": 9,
				"usability": 9,
				"performance": 9,
				"battery": 8
			}
	for i,j in zip(randnums,obj['meta']['aps-product-rating']):
		obj['meta']['aps-product-rating'][j]=int(str(i))
	
	obj['meta']["aps-product-rating-total"]= f"{np.average(randnums)}"
	obj['comment_status']="open"
	features=soup.find_all('div',{'class':'aps-feature-anim'})
	obj['aps-product-features']=[]
	for ele in features:
		feature={}
		feature['icon']=ele.select('span',{'class':'aps-list-icon'})[0]['class'][1].replace('aps-icon-','')
		feature['name']=features_names[feature['icon']]
		feature['value']=ele.select('span',{'class':'aps-list-icon'})[1].text
		obj['aps-product-features'].append(feature)
	obj['terms']={}
		#print(ele.select('div',{'class':'aps-feature-info'}))
	obj['terms']['aps-brands']=['samsung']
	obj['terms']['aps-cats']=["%d9%87%d9%88%d8%a7%d8%aa%d9%81-%d8%b0%d9%83%d9%8a%d8%a9"]
	content=soup.find_all('div',{'id':'aps-overview'})
	content_p=content[0].find_all('div',{'aps-column'})[1].find_all('p')
	# print(len(content[0].find_all('div',{'aps-column'})[1].find_all('p')))
	obj['content']=''
	for i in content_p:
		if i.text!='':
			obj['content']=obj['content']+i.text

		#aps-group
	groups=soup.find_all('div',{'class':'aps-group'})
	for group in groups:
		for j in group.find_all('span',{'class':'aps-1co'}):
			if j.find_all('i'):
				if j.find_all('i',{'class':''})
			aps-icon-check
			aps-icon-cancel 
			else:




	break
	products.append(obj)













data=json.dumps(products,indent=4)
# x=open('samsung_products.json','w+')
# x.write(data)
# x.close()
# print("done")

