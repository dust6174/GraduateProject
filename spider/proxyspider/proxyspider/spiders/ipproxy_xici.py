# -*- coding: utf-8 -*-
import scrapy
from proxyspider.items import IpProxyItem


class IpproxySpider(scrapy.Spider):
    name = 'ipproxy_xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://xicidaili.com/']

    def start_requests(self):
        url_list = []
        for i in range(20, 21):
            url = 'http://www.xicidaili.com/nn/%d' % i
            req = scrapy.Request(url)
            # 存储所有对应地址的请求
            url_list.append(req)
        return url_list

    def parse(self, response):
        table = response.xpath('//table[@id="ip_list"]')[0]
        trs = table.xpath('//tr')[1:]  # 去掉标题行
        items = []
        for tr in trs:
            ip_proxy = IpProxyItem()
            ip_proxy['ip_address'] = tr.xpath('td[2]/text()').extract()[0]
            ip_proxy['port'] = tr.xpath('td[3]/text()').extract()[0]
            items.append(ip_proxy)
        return items
