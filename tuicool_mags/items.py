# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy
#
#
#class TuicoolMagsItem(scrapy.Item):
#    # define the fields for your item here like:
#    # name = scrapy.Field()
#    pass
from scrapy.item import Item,Field

class ArticleItem(Item):
  title=Field()  #标题
  timetamp=Field()  #时间
  site=Field()  #社区
  source=Field()  #来源
  topic=Field()  #主题
  article_body=Field()  #文章
  mag_title=Field()  #所在期刊名
  mag_datetime=Field()  #所在期刊的发行时间
  belongto=Field()  #所属类（项目报道，创业路上...)
  tuicool_id=Field()  #在tuicool的id

class MaganizeItem(Item):
  title=Field()   #期刊名
  datetime=Field()  #出版时间
  href=Field()  #网址
