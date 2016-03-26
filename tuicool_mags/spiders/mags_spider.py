# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor 
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
from tuicool_mags.items import *

class MagsSpider(CrawlSpider):
  name="mags"
  allowed_domains=["tuicool.com"]
  start_urls=[
    "http://www.tuicool.com/mags/",
    "http://www.tuicool.com/mags/design/",
    "http://www.tuicool.com/mags/startup/",
    "http://www.tuicool.com/mags/tech/"
  ]
  
  rules=(
    Rule(LinkExtractor(allow=("http://www.tuicool.com/mags/.+/.+",)),callback="get_info_mag"),
    Rule(LinkExtractor(allow=("http://www.tuicool.com/mags",)),callback="parse_mag"),
    Rule(LinkExtractor(allow=("http://www.tuicool.com/articles",)),callback="parse_article"),
    )

  def parse_mag(self,response):
    sel=Selector(response=response)
    print("22222222222")
    print(response)
    item_li=sel.xpath("//div[@class='mag zhoukan_mag']")[0].xpath("./ul/li")
    print("1111111111111111111111111111111111")
    print(item)
    asdfasdfasdfasdfa
    for li in item_li:
      item=MaganizeItem()
      item["href"]=li.xpath("./a/@href")[0].strip()
      item["title"]=li.xpath("./a/span[@class='mag-title']/text()")[0].strip()
      item["datetime"]=li.xpath("./a/span[@class='mag-tip']/text()")[0].strip()
      yield item
      yield scrapy.Request(item["href"],self.get_info_mag)

  def get_info_mag(self,response):
    sel=Selector(response=response)
    mag_div=sel.xpath("//div[@class='mag mag_detail']")[0]
    mag_title=mag_div.xpath("./div/h3/text()")[0].strip()
    mag_datetime=mag_div.xpath("./div/h3/sub/text()")[0].strip()
    article_ul=mag_div.xpath("./ul")
    article_ol=mag_div.xpath("./ol")
    for i in range(0,len(article_ol)):
      ul=article_ul[i]
      ol=article_ol[i] 
      belongto=ul.xpath("./li/strong/text()")[0].strip()
      for li in ol.xpath("./li"):
        item=ArticleItem()
        item["mag_title"]=mag_title
        item["mag_datetime"]=mag_datetime
        item["belongto"]=belongto
        item["tuicool_id"]=li.xpath("./h4/a/@href")[0].split("=")[-1].strip()
        yield scrapy.Request("http://www.tuicool.com/articles/"+item["tuicool_id"],self.parse_article,meta={"item":item})

  def parse_article(self,response):
    sel=Selector(response)
    item=response.meta["item"]
    art_div=sel.xpath("//div[@class='span8 contant article_detail_bg']")[0]
    item["title"]=art_div.xpath("./h1/text()")[0].strip()
    item["timetamp"]=art_div.xpath("./div[@class='article_meta']/div/span[@class='timestamp']/text()")[0].strip()
    item["site"]=art_div.xpath("./div[@class='article_meta']/div/span[@class='from']/a/text()")[0].strip()
    item["source"]=art_div.xpath("./div[@class='article_meta']/div[@class='source']/a/@href")[0].strip()
    item["topic"]=""
    a_topic=art_div.xpath("./div[@class='article_meta']/div")[-1].xpath("./a")
    for a in a_topic:
      item["topic"]=item["topic"]+" "+a.xpath("./span/text()")[0]
    art_body_div=sel.xpath("//div[@class='article_body']/div")[0]
    item["article_body"]=lxml.html.tostring(art_body_div)
    return item








































# # -*- coding: utf-8 -*-
# from scrapy.spider import BaseSpider
# import requests
# import lxml
# import json
# from tuicool_mags.items import *

# class MagsSpider(BaseSpider):
#   name="mags"
#   allowed_domains=["tuicool.com"]
#   start_urls=[
#     "http://www.tuicool.com/mags/",
#     "http://www.tuicool.com/mags/design/",
#     "http://www.tuicool.com/mags/startup/",
#     "http://www.tuicool.com/mags/tech/"
#   ]

#   handle_httpstatus_list = [503]

#   def parse(self,response):
#     r=requests.get(response.url)
#     if r.status_code!=200:return False
#     html=lxml.html.fromstring(r.text)
#     item_li=html.xpath("//div[@class='mag zhoukan_mag']")[0].xpath("./ul/li")
#     items=[]
#     for li in item_li:
#       item=MaganizeItem()
#       item["href"]=li.xpath("./a/@href")[0].strip()
#       item["title"]=li.xpath("./a/span[@class='mag-title']/text()")[0].strip()
#       item["datetime"]=li.xpath("./a/span[@class='mag-tip']/text()")[0].strip()
#       print("****")
#       print(item)
#       items.append(item)
#       try:
#         f=open("/root/tuicool_mags/mags.json","ab")
#         f.write(json.dumps(dict(item)) + "\n")
#       except:
#         pass
#       finally:
#         f.close()
#       self.crawling_articles(item["href"])
#     return items

#   def crawling_articles(self,url):
#     '''
#       根据抓到的每一期的期刊地址，抓取其下的文章
#     '''
#     r=requests.get("http://www.tuicool.com"+url)
#     if r.status_code!=200: return False
#     items=[]
#     html=lxml.html.fromstring(r.text)
#     item_div=html.xpath("//div[@class='mag mag_detail']")[0]
#     mag_title=item_div.xpath("./div/h3/text()")[0].strip()
#     mag_datetime=item_div.xpath("./div/h3/sub/text()")[0].strip()
#     item_ul=item_div.xpath("./ul")
#     item_ol=item_div.xpath("./ol")
#     if len(item_ul)!=len(item_ol): return False
#     for i in range(0,len(item_ol)):
#       ul=item_ul[i]
#       ol=item_ol[i]
#       belongto=ul.xpath("./li/strong/text()")[0].strip()
#       for li in ol.xpath("./li"):
#         try:
#           item=ArticleItem()
#           item["mag_title"]=mag_title
#           item["mag_datetime"]=mag_datetime
#           item["belongto"]=belongto
#           item["tuicool_id"]=li.xpath("./h4/a/@href")[0].split("=")[-1].strip()
#           url2="http://www.tuicool.com/articles/"+item["tuicool_id"].strip()
#           proxies={'http': 'http://1.36.208.153:80'}
#           headers={"User-Agant":'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}
#           r_article=requests.get(url2,proxies=proxies,headers=headers)
#           print("1111111111111111111111111111")
#           print(item["tuicool_id"])
#           print(url2)
#           print(r_article.status_code)
#           if r_article.status_code!=200: continue
#           h_article=lxml.html.fromstring(r_article.text)
#           art_div=h_article.xpath("//div[@class='span8 contant article_detail_bg']")[0]
#           item["title"]=art_div.xpath("./h1/text()")[0].strip()
#           item["timetamp"]=art_div.xpath("./div[@class='article_meta']/div/span[@class='timestamp']/text()")[0].strip()
#           item["site"]=art_div.xpath("./div[@class='article_meta']/div/span[@class='from']/a/text()")[0].strip()
#           item["source"]=art_div.xpath("./div[@class='article_meta']/div[@class='source']/a/@href")[0].strip()
#           item["topic"]=""
#           a_topic=art_div.xpath("./div[@class='article_meta']/div")[-1].xpath("./a")
#           for a in a_topic:
#             item["topic"]=item["topic"]+" "+a.xpath("./span/text()")[0]
#           art_body_div=h_article.xpath("//div[@class='article_body']/div")[0] 
#           item["article_body"]=lxml.html.tostring(art_body_div)
#           items.append(item)
#           try:
#             f=open("/root/tuicool_mags/articles.json","ab")
#             f.write(json.dumps(dict(item)) + "\n")
#           except:
#             pass
#           finally:
#             f.close()
#         except:
#           continue
#     return items
