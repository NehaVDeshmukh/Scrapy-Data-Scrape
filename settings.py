# -*- coding: utf-8 -*-

# Scrapy settings for gnews project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'gnews'

SPIDER_MODULES = ['gnews.spiders']
NEWSPIDER_MODULE = 'gnews.spiders'
ITEM_PIPELINES=['gnews.pipelines.GnewsPipeline']
#DOWNLOAD_DELAY=3
#COOKIES_ENABLED=False
#DUPEFILTER=True
#RANDOMIZE_DOWNLOAD_DELAY=True
#SCHEDULER_ORDER='BFO'
#DOWNLOADER_MIDDLEWARES = {
        #scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        #'gnews.comm.rotate_useragent.RotateUserAgentMiddleware' :400
    #}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gnews (+http://www.yourdomain.com)'
