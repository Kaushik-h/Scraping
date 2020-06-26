import scrapy


class ENgadget(scrapy.Spider):

    name = "engadget"

    start_urls = [
        "https://www.engadget.com//all/page/1",
        "https://www.engadget.com//all/page/2"
    ]
    
       
    def parse(self,response):
        c=0
        r = response.xpath("//div[@class='grid@m+']")
        article=response.xpath("//article")
        dom="https://www.engadget.com"
        for each in r:
             yield{
                    "url" : dom+each.xpath(".//h2/a/@href").extract_first(),
                    "img" : each.xpath(".//img/@src").extract_first(),
                    "title": each.xpath(".//h2/a/span/text()").extract_first(),
                    "des" : each.xpath(".//p/text()").extract_first(),
                    "time":each.xpath(".//span[@class=' hide@']/text()").extract_first()
              }
             break
       
        
        for each in article:
             c=c+1
             if c==1:
                 continue            
             
             
             yield{
                    "url" : dom+each.xpath("./a/@href").extract_first(),
                    "img" : each.xpath(".//div[@class='o-rating_thumb c-white']/img/@data-original").extract_first(),
                    "title" :each.xpath(".//h2/span/text()").extract_first(),
                    "des" : each.xpath(".//p/text()").extract_first(),
                    "time":each.xpath(".//div[@class='t-meta th-meta inline-block hide@tl+ hide@m-']/text()[2]").extract_first()
              }    
        
              

