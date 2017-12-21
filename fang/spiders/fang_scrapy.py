# -*- coding: utf-8 -*-
import scrapy
from fang.items import FangItem


class FangScrapySpider(scrapy.Spider):
    name = 'fang_scrapy'
    allowed_domains = ["fang.com"]
    #start_urls = ['http://esf.jn.fang.com']
    content_page_url="http://esf.jn.fang.com{}"



    def start_requests(self):
        for id in range(31,34):
            url_template="http://esf.jn.fang.com/house/i{}/"
            yield scrapy.Request(url=url_template.format(id),callback=self.parse,dont_filter=True)

    def parse(self,response):
        for href in response.xpath('//*[@class="title"]/a/@href').extract():
            detail_url=self.content_page_url.format(href)
            yield scrapy.Request(url=detail_url,callback=self.fang_details,dont_filter=True)
        # for url in urls:
        #     #fang_detail_url = 'http://esf.jn.fang.com' + ''.join(item['url'])
        #     #拼接房源的完整url;
        #     fang_detail_url = 'http://esf.jn.fang.com'+url
        #     #item['url']=fang_detail_url
        #     #print(item['url'])
        #     yield scrapy.Request(url=fang_detail_url,headers={'User-agent': 'Mozilla/5.0'},callback=self.fang_details)

    def fang_details(self,response):
        item=FangItem()
        #获取房源的描述title;
        item['title']=response.xpath('//*[@id="lpname"]/text()').extract()
        #获取房源的户型rooms;
        item['rooms']=response.xpath('/html/body/div[5]/div[1]/div[3]/div[3]/div[1]/div[1]/text()').extract()
        #获取房源的建筑面积floorage;
        item['floorage']=response.xpath('/html/body/div[5]/div[1]/div[3]/div[3]/div[2]/div[1]/text()').extract()
        #获取房源的小区名称housin_estate;
        item['housin_estate']=response.xpath('//*[@id="agantesfxq_C03_05"]/text()').extract()
        #获取房源总价;
        item['price_num']=response.xpath('/html/body/div[5]/div[1]/div[3]/div[2]/div[1]/i/text()').extract()
        #获取小区地址address;

        #获取房源编码house_code;

        #获取房源的单价price_unit_num;
        item['price_unit_num']=response.xpath('/html/body/div[5]/div[1]/div[3]/div[3]/div[3]/div[1]/text()').extract()
        #获取房源楼层floor;
        item['floor']=response.xpath('/html/body/div[5]/div[1]/div[3]/div[4]/div[2]/div[1]/text()').extract()
        #获取房源的年限term;

        #获取房源的建成时间year;
        item['year']=response.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/span[2]/text()').extract()
        #获取房源的朝向orientation;
        item['orientation']=response.xpath('/html/body/div[5]/div[1]/div[3]/div[4]/div[1]/div[1]/text()').extract()
        #获取房源的标签tags;
        #item['tags']=response.xpath('/html/body/div[5]/div[1]/div[3]/div[2]/div[6]/text()').extract()
        #获取房房源的城市city;

        #获取房源的区域district;
        #item['district']=response.xpath('//*[@id="address"]/text()').extract()
        #获取房源的decoration_situation;

        yield item



