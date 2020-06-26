import scrapy
import requests


class Newsy(scrapy.Spider):

    name = "lap"

    start_urls=["https://www.nologygate.com/i-life-laptops"]
    # start_urls=[]
    # for i in range(2,39):
    #     lurl=lapurl
    #     lurl=lurl.replace('*',str(i))
    #     start_urls.append(lurl)


    def parse(self,response):
        r = response.xpath("//div[@class='product']")
        for each in r:
                a=each.xpath(".//a/@href").extract_first()
                code=requests.get(a)
                #print(code.text)
                str=a[34:]
                # brand=str.split("-",1)[0]
                brand="i-life"
                # if brand=="i":
                #     continue
                lapname=str.split("-",2)[2]
                html_handle=open(f'html\{brand}\{lapname}.html','w+',encoding="utf-8")
                html_handle.write(code.text)
                html_handle.close()


        
    		
            # yield{
            #         "url" : each.xpath("./@href").extract_first(),
            #         "image":'null',
            #         "title" :each.xpath("./text()").extract_first(),
            #         "des" : 'null',
            #         "time": time.xpath("./a/text()").extract_first()
            #     }    
        
                  



			


               
        
                  

