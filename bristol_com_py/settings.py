# -*- coding: utf-8 -*-

# Scrapy settings for clickoffice_com_ar project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bristol_com_py'

SPIDER_MODULES = ['bristol_com_py.spiders']
NEWSPIDER_MODULE = 'bristol_com_py.spiders'


USER_AGENT = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36')
COOKIES_ENABLED = False

CONCURRENT_REQUESTS_PER_DOMAIN = 2
DOWNLOAD_DELAY = 0.5