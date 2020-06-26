import scrapy


class Roadtovr(scrapy.Spider):

    name = "roadtovr"

    start_urls = [
        "https://www.roadtovr.com"
    ]
       
    def parse(self,response):
        r = response.xpath("//div[@class='td_block_inner td-column-2'][1]//div[@class='td-animation-stack-type0-2 td_rtvr_module_10 td_module_wrap td-animation-stack']")
        for each in r:
            #print(each.xpath(".//time/@datetime").extract_first())
            yield{
                    "url" : each.xpath(".//h3/a/@href").extract_first(),
                    "image":each.xpath(".//img/@src").extract_first(),
                    "title" :each.xpath(".//h3/a/text()").extract_first(),
                    "des" : each.xpath(".//div[@class='td-excerpt']/text()").extract_first(),
                    "time":each.xpath(".//time/@datetime").extract_first()
                }    
        
                  

