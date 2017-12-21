# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangItem(scrapy.Item):
    domain = scrapy.Field()
    title = scrapy.Field()                    #房源的描述信息
    housin_estate = scrapy.Field()            #小区名称
    price_num = scrapy.Field()                #房源总价
    address = scrapy.Field()                  #小区地址
    rooms = scrapy.Field()                    #户型介绍
    house_code = scrapy.Field()               #房源编码
    url = scrapy.Field()                      #房源url
    floorage = scrapy.Field()                 #房源建筑面积
    decoration_situation = scrapy.Field()
    price_unit_num = scrapy.Field()           #房源单价
    floor = scrapy.Field()                    #楼层
    term = scrapy.Field()                     #小区年限
    year = scrapy.Field()                     #小区建成时间
    orientation = scrapy.Field()              #朝向
    tags = scrapy.Field()                     #标签
    city = scrapy.Field()                     #城市
    district = scrapy.Field()                 #区域
