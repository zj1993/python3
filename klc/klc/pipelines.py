# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
import json
from openpyxl import Workbook

class KlcPipeline(object):
    def __init__(self):
        # self.file = open('data.json', 'w', encoding='utf-8')
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['项目名称','项目详情','历史收益率','项目期限','项目金额','项目进度','项目进度百分比'])

    def process_item(self, item, spider):
        # # 读取item中的数据
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # # 写入文件
        # self.file.write(line)
        # # 返回item
        # return item
        line = [item['title'],item['url'],item['yearMoney'],item['day'],item['money'],item['progress'],item['percent']]
        self.ws.append(line)
        self.wb.save('klc.xlsx')
        return item

        # 该方法在spider被开启时被调用。

    def open_spider(self, spider):
        pass

        # 该方法在spider被关闭时被调用。

    def close_spider(self, spider):
        pass
