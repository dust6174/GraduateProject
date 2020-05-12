# -*- coding: utf-8 -*-
import scrapy
from proxyspider.items import IpProxyItem

class IpproxyKuaiSpider(scrapy.Spider):
    name = 'ipproxy_kuai'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://kuaidaili.com/']

    def start_requests(self):
        url_list = []
        for i in range(1, 40):
            url = 'https://www.kuaidaili.com/free/inha/%d' % i
            req = scrapy.Request(url)
            # 存储所有对应地址的请求
            url_list.append(req)
        return url_list

    def parse(self, response):
        trs = response.xpath('/html/body/div/div[4]/div[2]/div/div[2]/table/tbody//tr')
        items = []
        for tr in trs:
            ip_proxy = IpProxyItem()
            ip_proxy['ip_address'] = tr.xpath('td[1]/text()').get()
            # /html/body/div/div[4]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]
            ip_proxy['port'] = tr.xpath('td[2]/text()').get()
            # /html/body/div/div[4]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]
            items.append(ip_proxy)
        return items