# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhiyouItem(scrapy.Item):
    # define the fields for your item here like:
    # 数据源
    data_source = scrapy.Field()
    # 数据采集时间
    timestamp = scrapy.Field()
    # 企业名
    company_name = scrapy.Field()
    # 浏览次数
    views = scrapy.Field()
    # 口号
    slogan = scrapy.Field()
    # 公司性质
    category = scrapy.Field()
    # 行业分类
    industry = scrapy.Field()
    # 企业简介
    desc = scrapy.Field()
    # 好评度
    praise = scrapy.Field()
    # 薪资
    salary = scrapy.Field()
    # 融资信息
    finance_info = scrapy.Field()
    # 地址信息
    address = scrapy.Field()
    # 练习方式
    contact = scrapy.Field()
    pass
