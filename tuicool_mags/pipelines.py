# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TuicoolMagsPipeline(object):
    def __init__(self):
        self.art_file=open("/root/tuicool_mags/articles.json","wb")
        self.mag_file=open("/root/tuicool_mags/mags.json","wb")
        print("11111111111111111111111111111111")
        print("11111111111111111111111111111111")
        print("11111111111111111111111111111111")
        print("11111111111111111111111111111111")
        print(item)

    def process_item(self, item, spider):
        line=json.dumps(dict(item))+"\n"
        # self.file.write(line)
        if item["tuicool_id"]:
          self.art_file.write(line)
        else:
          self.mag_file.write(line)
        return item
