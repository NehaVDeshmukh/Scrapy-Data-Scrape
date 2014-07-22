import scrapy
from gnews.items import GnewsItem
class NewsSpider(scrapy.Spider):
    name ="spidy"
    '''allowed_domains = ["dmoz.org"]
    start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"] '''
    start_urls=['https://news.google.com/?ar=1405967412']

    def parse(self,response):
        
        item=GnewsItem()
        catitem=GnewsItem()
        
        div1=response.xpath('//div[@class="section top-stories-section"]') 
            
        for sel in div1.xpath('.//div[starts-with(@class,"blended-wrapper")]'):
                
                item['topstory']=sel.xpath('.//h2//span/text()').extract()
                item['link']=sel.xpath('.//h2//@href').extract()
                item['originallink']=sel.xpath('.//h2//@url').extract()
                item['category']=div1.xpath('.//span[@class="section-name"]/text()').extract()
                item['snippet']=sel.xpath('.//div[@class="esc-lead-snippet-wrapper"]/text()').extract()
                item['sublinks']=sel.xpath('.//div[@class="esc-secondary-article-wrapper"]//@url').extract()
                item['gpost']=sel.xpath('.//div[@class="gpost-body"]//@href').extract()
                item['gpostsnip']=sel.xpath('.//div[@class="gpost-body"]//text()').extract()
                item['related']=sel.xpath('.//div//span//a[@class="esc-topic-link"]//@href').extract()
                item['extras']=sel.xpath('.//div[@class="esc-diversity-wrapper"]//span/text()').extract()
                item['extraslink']=sel.xpath('.//div[@class="esc-diversity-wrapper"]//@href').extract()
                yield item
        
        div2=response.xpath('//div[starts-with(@class,"section story-section")]')
        
        for sel1 in div2.xpath('.//div[starts-with(@class,"blended-wrapper")]'):
            
                catitem['topstory']=sel1.xpath('.//h2//span[@class="titletext"]/text()').extract()
                catitem['link']=sel1.xpath('.//h2//@href').extract()
                catitem['originallink']=sel1.xpath('.//h2//@url').extract()
                catitem['category']=sel1.xpath('./preceding-sibling::div[@class="section-header"]//span[@class="section-name"]/text()').extract()
                catitem['snippet']=sel1.xpath('.//div[@class="esc-lead-snippet-wrapper"]/text()').extract()
                catitem['sublinks']=sel1.xpath('.//div[@class="esc-secondary-article-wrapper"]//@url').extract()
                catitem['gpost']=sel1.xpath('.//div[@class="gpost-body"]//@href').extract()
                catitem['gpostsnip']=sel1.xpath('.//div[@class="gpost-body"]//text()').extract()
                catitem['related']=sel1.xpath('.//div//span//a[@class="esc-topic-link"]//@href').extract()
                catitem['extras']=sel1.xpath('.//div[@class="esc-diversity-wrapper"]//span/text()').extract()
                catitem['extraslink']=sel1.xpath('.//div[@class="esc-diversity-wrapper"]//@href').extract()
                yield catitem
                
            