# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KlcItem(scrapy.Item):
    # 项目地址
    url = scrapy.Field()
    # 项目名称
    title = scrapy.Field()
    # 历史收益率
    yearMoney = scrapy.Field()
    # 项目期限
    day = scrapy.Field()
    # 项目金额
    money = scrapy.Field()
    # 项目进度
    progress = scrapy.Field()
    # 进度百分比
    percent = scrapy.Field()
