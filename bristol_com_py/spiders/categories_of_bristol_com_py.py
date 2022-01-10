import scrapy, re, json
from urlparse import urlparse

class CategoriesOfbristol_com_py(scrapy.Spider):

	name = "categories_of_bristol_com_py"
	start_urls = ('https://bristol.com.py/',)

	use_selenium = False
	def parse(self, response):
		categories = response.xpath('//li[@class="dropdown show-on-hover" or @class="category-item show-on-hover"]/ul/li/ul/li/a/@href').extract()
		yield {'links':list(x for x in categories)}
