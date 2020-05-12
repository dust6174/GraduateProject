# -*- coding: utf-8 -*-
import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TCPTimedOutError
from microdistrictspider.items import MicrodistrictItem

class MicrodistrictShSpider(scrapy.Spider):
    name = 'microdistrict_sh'
    allowed_domains = ['sh.lianjia.com']
    start_urls = ['https://sh.lianjia.com/xiaoqu/cro21/']

    def parse(self, response):
        base_url = 'https://sh.lianjia.com'
        for region in response.xpath("/html/body/div[3]/div[1]/dl[2]/dd/div/div//a/@href").getall():
            region_url = base_url+region
            yield scrapy.Request(region_url,callback=self.parse_zone)

    def parse_zone(self,response):
        base_url = 'https://sh.lianjia.com'
        for region in response.xpath("/html/body/div[3]/div[1]/dl[2]/dd/div/div[2]//a/@href").getall():
            region_url = base_url+region
            yield scrapy.Request(region_url,callback=self.parse_list)

    def parse_list(self,response):
        microdistrict_list = response.xpath("/html/body/div[4]/div[1]/ul//li/div[1]/div[1]/a/text()").getall()
        for microdistrict in microdistrict_list:
            item = MicrodistrictItem()
            item['name'] = microdistrict
            yield item
        if "下一页" == response.xpath("/html/body/div[4]/div[1]/div[3]/div[2]/div/a[last()]/text()").get() :
            next_page = response.xpath("/html/body/div[4]/div[1]/div[3]/div[2]/div/a[last()]/@href").get()
            yield  scrapy.Request(next_page,callback=self.parse_list,errback=self.errback_logandretry)

    def errback_logandretry(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

        yield scrapy.Request(request.url,callback=self.parse_list,errback=self.errback_logandretry)