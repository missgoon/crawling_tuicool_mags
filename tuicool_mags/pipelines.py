# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TuicoolMagsPipeline(object):
  def __init__(self):
      self.art_file=open("/root/tuicool_mags/articles.json","wb")
      self.mag_file=open("/root/tuicool_mags/mags.json","wb")
      self.all_file=open("/root/tuicool_mags/all.json","wb")

  def process_item(self, item, spider):
      line=json.dumps(dict(item))+"\n"
      # self.file.write(line)
      if item.get("tuicool_id","false")!="false":
        print("ok..............................mags")
        self.art_file.write(line)
      elif item.get("href","false")!="false":
        print("ok....................art")
        self.mag_file.write(line)
      else:
        print("ok........................error")
        self.all_file.write(line)
      return item

  def close_spider(self,spider):
    print("ok you're closing spider")
    self.art_file.close()
    self.mag_file.close()
