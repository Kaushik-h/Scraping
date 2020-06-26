import scrapy


class Newsy(scrapy.Spider):

    name = "newsy"

    start_urls = [
        "https://news.ycombinator.com/"
    ]
       
    def parse(self,response):
        r = response.xpath("//a[@class='storylink']")
        s = response.xpath("//span[@class='age']")
        for each, time in zip(r, s):
            #print(time.xpath("./a/text()").extract_first())
            yield{
                    "url" : each.xpath("./@href").extract_first(),
                    "image":'null',
                    "title" :each.xpath("./text()").extract_first(),
                    "des" : 'null',
                    "time": time.xpath("./a/text()").extract_first()
                }    
        
                  

