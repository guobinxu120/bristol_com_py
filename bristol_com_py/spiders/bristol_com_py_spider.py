# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
from scrapy import Request, FormRequest
from urlparse import urlparse
from datetime import date
import json, requests
import re
import time
import datetime
class bristol_com_pySpider(scrapy.Spider):

    name = "bristol_com_py_spider"

    use_selenium = False

    total_urls = []

###########################################################

    def __init__(self, categories=None, *args, **kwargs):
        super(bristol_com_pySpider, self).__init__(*args, **kwargs)

        if not categories:
            raise CloseSpider('Received no categories!')
        else:
            self.categories = categories
        self.start_urls = json.loads(self.categories).keys()

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
        }

###########################################################

    def start_requests(self):
        for url in self.start_urls:
            yield Request(('https://bristol.com.py/') + url, callback=self.parse, meta={'CatURL':url, 'page_count': 1})

###########################################################

    def parse(self, response):
        products = response.xpath('//div[@class="product-item-box"]/a')

        #print len(products)
        if not products: return

        for i in products:
            item = {}
            item['Vendedor'] = 512
            item['ID'] = i.xpath('./@href').extract_first().split('-')[-1]
            item['Title'] = i.xpath('./h3/text()').extract_first()

            price = i.xpath('.//span[@class="precio-actual"]/text()').re(r'[\d.,]+')

            if price:
                if price[0] == '.':
                    item['Price'] = price[1].replace('.', '')
                else:
                    item['Price'] = price[0].replace('.', '')
                item['Currency'] = 'GS'

                item['Category URL'] = response.meta['CatURL']
                item['Details URL'] = response.urljoin(i.xpath('./@href').extract_first())
                item['Date'] = date.today()

                item['timestamp'] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                item['image_url'] = response.urljoin(i.xpath('./img/@src').extract_first())

                if item['Details URL'] in self.total_urls:
                    continue
                self.total_urls.append(item['Details URL'])

                yield item

        response.meta['page_count'] += 1
        next_url = 'https://bristol.com.py/' + response.meta['CatURL'] + '.' + str(response.meta['page_count'])
        if next_url:
            yield Request(response.urljoin(next_url), callback=self.parse, meta=response.meta)
