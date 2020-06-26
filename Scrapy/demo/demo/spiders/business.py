import scrapy


class Business(scrapy.Spider):

    name = "business"

    start_urls = [
        "https://www.businessinsider.com/sai?r=US&IR=T"
    ]
       
    def parse(self,response):
        dom="https://www.businessinsider.com"


        res = response.xpath("//section[@id='l-content']")    

        r=res.xpath(".//section[@class='river-item default-tout js-feed-item']")
        s=res.xpath(".//div[@class='tout-tag d-lg-flex']")
        
        for each, time in zip(r, s):
            str=(each.xpath(".//img/@data-srcs").extract_first())
            imgurl= list(eval(str).keys())[0]
            print(imgurl)

            yield{
                    "url" : dom+each.xpath(".//h2/a/@href").extract_first(),
                    "image" :imgurl,
                    "title" :each.xpath(".//h2/a/text()").extract_first(),
                    "des" : each.xpath(".//div[@class='tout-copy river']/text()").extract_first(),
                    "time":time.xpath("./span/text()").extract_first()
                }    
        
                  

