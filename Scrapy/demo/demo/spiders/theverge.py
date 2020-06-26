import scrapy
from datetime import datetime,timedelta


class THEverge(scrapy.Spider):

    name = "theverge"

    start_urls = [
        "https://theverge.com/"
    ]
       
    def parse(self,response):
        r = response.xpath("//div[@class='c-entry-box--compact c-entry-box--compact--article']")
        
        for each in r:
           a=each.xpath(".//div/div/span/span[2]/time/@datetime").extract_first()
        #    b=datetime.now()
        #    d1 = datetime.strptime(a,"%Y-%m-%dT%H:%M:%S")+timedelta(hours=5,minutes=30)
        #    dif=b-d1
        #    #print(b)
        #    ans=dif.total_seconds()/3600
        #    #date_a= datetime.strptime(a,'%m-%d-%y %H:%M:%S')
        #    print(d1)
        #    #print(ans)
        #    if ans<12.0:
           yield{
                        "url" : each.xpath(".//h2/a/@href").extract_first(),
                        "image" : each.xpath(".//a/div/noscript/img/@src").extract_first(),
                        "title" :each.xpath(".//h2/a/text()").extract_first(),
                        "time":a
                    }    
        
                  

