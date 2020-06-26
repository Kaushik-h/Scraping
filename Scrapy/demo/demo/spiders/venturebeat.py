import scrapy
from datetime import datetime,timedelta


class Venturebeat(scrapy.Spider):

    name = "venturebeat"

    start_urls = [
        "https://venturebeat.com/"
    ]
       
    def parse(self,response):
        r = response.xpath("//div[@class='MainBlock__river story-river']/article")
        
        for each in r:
           a=each.xpath(".//time/@datetime").extract_first()
        #    d1 = datetime.now()
        #    d2 = datetime.strptime(a,"%Y-%m-%dT%H:%M:%S-07:00")+timedelta(hours=7)
        #    ans=(d1-d2)
        
           yield{
                        "url" : each.xpath("./a/@href").extract_first(),
                        "title" :each.xpath(".//h2/a/text()").extract_first(),
                        "image" : each.xpath("./a/img/@src").extract_first(),
                        "time":a
                    }    
        
                  

