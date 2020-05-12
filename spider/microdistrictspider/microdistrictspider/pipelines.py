# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MicrodistrictspiderPipeline:
    def process_item(self, item, spider):
        self.out_file.write(item['name']+'\n')
        return item

    def open_spider(self,spider):
        print("storage file opening...")
        storage_path = "H:/codes/graduateProject/data/source/microdistrict/"
        self.out_file = open(storage_path+spider.name+".txt",'w')
        # if spider.name == "microdistrict_bj":
        #     self.out_file = open(storage_path+"microdistrict_bj.txt",'w')
        # elif spider.name == "microdistrict_sh":
        #     self.out_file = open(storage_path+"microdistrict_sh.txt",'w')
        # elif spider.name == "microdistrict_gz":
        #     self.out_file = open(storage_path+"microdistrict_gz.txt",'w')
        # elif spider.name == "microdistrict_sz":
        #     self.out_file = open(storage_path+"microdistrict_sz.txt",'w')
    def close_spider(self,spider):
        self.out_file.close()
        print("storage file closed...")
