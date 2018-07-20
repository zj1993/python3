# -*- coding: utf-8 -*-

import scrapy

from ..items import KlcItem

class Klc(scrapy.Spider):
    # 用于区别Spider
    name = 'Klc'
    # 允许访问的域
    allowed_domains = ['58klc.com']
    # 爬取的网址
    start_urls = ["https://www.58klc.com/Borrow/index"]

    # 爬取的方法
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = KlcItem()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        #
        for box in response.xpath('//div[@class="invest-items"]/a'):
            #
            item['url'] = 'https://www.58klc.com' + box.xpath('.//@href').extract()[0]
            #
            item['title'] = box.xpath('.//div[1]/@title').extract()[0].strip()
            #
            item['yearMoney'] = box.xpath('.//div[@class="year-money"]/p/span/text()').extract()[0].strip()
            #
            item['day'] = box.xpath('.//div[@class="project-day"]/div[1]/span/text()').extract()[0]
            #
            item['money'] = box.xpath('.//div[@class="project-day"]/div[2]/span/text()').extract()[0]
            #
            item['progress'] = box.xpath('.//span[1]/text()').extract()[3].strip()
            #
            item['percent'] = box.xpath('.//span[2]/text()').extract()[3].strip()
            # # 返回信息
            # print(item)
            yield item
        #跟进url
        #获取下一页的url信息
        url = response.xpath('.//div[@id="pages"]/div/a[@class="next"]/@href').extract()

        if url :
            #将信息组合成下一页的url
            page = 'https://www.58klc.com/' + url[0]
            #返回url
            yield scrapy.Request(page, callback=self.parse)
#         #url跟进结束
