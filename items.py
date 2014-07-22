# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GnewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topstory=scrapy.Field()
    snippet=scrapy.Field()
    link=scrapy.Field()
    originallink=scrapy.Field()
    sublinks=scrapy.Field()
    sublinktext=scrapy.Field()
    category=scrapy.Field()
    gpost=scrapy.Field()
    gpostsnip=scrapy.Field()
    extras=scrapy.Field()
    related=scrapy.Field()
    extraslink=scrapy.Field()
    videolinks=scrapy.Field()
'''class DmozItem(scrapy.Item):
        title = scrapy.Field()
        link = scrapy.Field()
        desc = scrapy.Field()'''
