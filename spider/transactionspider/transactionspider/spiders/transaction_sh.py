# -*- coding: utf-8 -*-
import scrapy
from transactionspider.items import TransactionItem


class TransactionShSpider(scrapy.Spider):
    name = 'transaction_sh'
    allowed_domains = ['sh.lianjia.com']
    start_urls = ['http://sh.lianjia.com/']

    def start_requests(self):
        url_list = []
        current_index = 22
        microdistrict_list = open('H:/codes/graduateProject/data/source/microdistrict/sh/microdistrict_sh_' + str(current_index) + '.txt','r').readlines()
        for microdistrict in microdistrict_list:
            url = 'https://sh.lianjia.com/chengjiao/rs' + microdistrict + '/'
            req = scrapy.Request(url)
            # 存储所有对应地址的请求
            url_list.append(req)
        return url_list

    def parse(self, response):
        # 如果所搜索小区有成交信息:
        # 将下一页的链接加入请求队列
        # if 链接列表最后一项的text() include '下一页': 判断下一页的URL和当前URL是否相等，如果不相等 则加入请求队列
        # else 如果当前是所搜索小区成交信息的第一页将url列表的除第一页外的所有项加入请求队列
        # 或者(当前采用)
        # 如果当前是所搜索小区成交信息的第一页的话 直接获取成交数量
        # 如果为0 跳过
        # 再用字符串拼接制作url机器如请求队列
        if response.xpath('/html/body/div[@class="content"]/div[@class="leftContent"]/div[@class="resultDes clear"]/div[@class="total fl"]/span/text()').get() is not None:
            transaction_count = int(response.xpath('/html/body/div[@class="content"]/div[@class="leftContent"]/div[@class="resultDes clear"]/div[@class="total fl"]/span/text()').get())
            if transaction_count != 0:
                # 信息提取
                transaction_list = response.xpath('/html/body/div[5]/div[1]/ul//li/div/div[1]/a/@href').getall()
                for transaction_url in transaction_list:
                    yield scrapy.Request(transaction_url,callback=self.parse_transaction)
                # 判断是否不止一页
                if transaction_count > 30:
                    # 判断是否是第一页
                    if "pg" not in response.request.url:
                        page_num = 0
                        if transaction_count % 30 == 0:
                            page_num = transaction_count // 30
                        else:
                            page_num = (transaction_count // 30) + 1
                        # 构造url并加入request queue
                        for num in range(2,page_num+1):
                            url = response.request.url.replace("rs","pg"+str(num)+"rs")
                            yield scrapy.Request(url, callback=self.parse)
        else:
            print("触发反爬虫机制")
            yield scrapy.Request(response.request.url,callback=self.parse)

    def parse_transaction(self,response):
        # 判断是否触发反爬虫机制
        if response.xpath("/html/body/section[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[1]/text()").get() is not None:
            transaction = TransactionItem()
            transaction['type'] = response.xpath("/html/body/section[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[1]/text()").get()
            transaction['area'] = response.xpath("/html/body/section[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/text()").get()
            transaction['orientation'] = response.xpath("/html/body/section[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[7]/text()").get()
            transaction['floor'] = response.xpath("/html/body/section[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/text()").get()
            transaction['age'] = response.xpath("/html/body/section[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[8]/text()").get()
            transaction['purpose'] = response.xpath("/html/body/section[2]/div[1]/div[1]/div[1]/div[2]/div[2]/ul/li[4]/text()").get()
            transaction['heating'] = response.xpath("/html/body/section[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[11]/text()").get()
            transaction['fitment'] = response.xpath("/html/body/section[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[9]/text()").get()
            transaction['elevator'] = response.xpath("/html/body/section[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[13]/text()").get()
            transaction['area_price'] = response.xpath("/html/body/section[2]/div[1]/div[2]/ul/li/p/text()").get()
            transaction['transaction_price'] = response.xpath("/html/body/section[1]/div[2]/div[2]/div[1]/span/i/text()").get()
            transaction['transaction_cycle'] = response.xpath("/html/body/section[1]/div[2]/div[2]/div[3]/span[2]/label/text()").get()
            transaction['listing_price'] = response.xpath("/html/body/section[1]/div[2]/div[2]/div[3]/span[1]/label/text()").get()
            transaction['views'] = response.xpath("/html/body/section[1]/div[2]/div[2]/div[3]/span[4]/label/text()").get()
            transaction['price_adjustment'] = response.xpath("/html/body/section[1]/div[2]/div[2]/div[3]/span[3]/label/text()").get()
            transaction['followers'] = response.xpath("/html/body/section[1]/div[2]/div[2]/div[3]/span[5]/label/text()").get()
            transaction['pageviews'] = response.xpath("/html/body/section[1]/div[2]/div[2]/div[3]/span[6]/label/text()").get()
            yield transaction

