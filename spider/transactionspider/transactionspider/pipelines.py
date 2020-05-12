# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime


class TransactionspiderPipeline:
    def process_item(self, item, spider):
        self.out_file.write(
            "|" + item['type'] + "|" + item['area'] + "|" + item['orientation'] + "|" + item['floor'] + "|" + item[
                'age'] + "|" + item['purpose'] + "|" + item['heating'] + "|" + item['fitment'] + "|" + item[
                'elevator'] + "|" + item['area_price'] + "|" + item['transaction_price'] + "|" + item[
                'transaction_cycle'] + "|" + item['listing_price'] + "|" + item['views'] + "|" + item[
                'price_adjustment'] + "|" + item['followers'] + "|" + item['pageviews'] + "|" + '\n')
        return item

    def open_spider(self, spider):
        print("storage file opening...")
        storage_path = "H:/codes/graduateProject/data/source/transaction/"
        current_index = 11
        self.out_file = open(storage_path +spider.name + '/' + spider.name + "_" + str(current_index) + ".txt", 'w')

    def close_spider(self, spider):
        self.out_file.close()
        print("storage file closed...")
