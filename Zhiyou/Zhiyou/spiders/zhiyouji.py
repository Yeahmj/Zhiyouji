# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Zhiyou.items import ZhiyouItem


class ZhiyoujiSpider(CrawlSpider):
    name = 'zhiyouji'
    allowed_domains = ['jobui.com']
    start_urls = ['http://www.jobui.com/cmp?area=%E5%85%A8%E5%9B%BD&keyword=']

    rules = (
        # 列表页面提取规则
        Rule(LinkExtractor(allow=r'/cmp\?area=%E5%85%A8%E5%9B%BD&n=\d+#listInter'), callback='parse_item', follow=True),
        # 详情页面url提取规则
        Rule(LinkExtractor(allow=r'/company/\d+/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print(response.url)
        # 创建存储数据的容器
        item = ZhiyouItem()

        # 抽取数据
        item['data_source'] = response.url
        item['timestamp'] = response.url

        # 从响应中抽取数据
        item['company_name'] = response.xpath('//*[@id="companyH1"]/a/text()').extract_first()
        item['views'] = response.xpath('//div[@class="fl ele fs16 gray9 mr10"]/text()').extract_first().split('人')[0].strip()
        item['slogan'] = response.xpath('//p[@class="fs16 gray9 sbox company-short-intro"]/text()').extract_first()
        item['category'] = response.xpath('//*[@id="cmp-intro"]/div/div[2]/dl/dd[1]').extract_first()
        item['industry'] = response.xpath('//*[@id="cmp-intro"]/div/div[2]/dl/dd[2]/a/text()').extract()
        item['desc'] = response.xpath('//*[@id="textShowMore"]/text()').extract_first()
        item['praise'] = response.xpath('//div[@class="swf-contA"]/div/h3/text()').extract_first()
        item['salary'] = response.xpath('//div[@class="swf-contB"]/div/h3/text()').extract_first()
        # print(item)

        # 获取融资情况
        node_list = response.xpath('//div[@class="jk-matter jk-box fs16"]/ul[@class="col-informlist"]/li')
        # print(len(node_list))
        data_list = []
        # 遍历节点列表抽取数据
        for node in node_list:
            temp = {}
            temp['date'] = node.xpath('./span[1]/text()').extract_first()
            temp['status'] = node.xpath('./h3/text()').extract_first()
            temp['sum'] = node.xpath('./span[2]/text()').extract_first()
            temp['investor'] = node.xpath('./span[3]/text()').extract_first()
            data_list.append(temp)
            # print(temp)

        item['finance_info'] = data_list

        item['address'] = response.xpath('//dl[@class="dlli fs16"]/dd[1]/text()').extract_first()
        item['address'] = response.xpath('//div[@class="j-shower1 dn"]/dd/text()').extract_first().replace('\xa0','')
        # print(item)

        # 返回给引擎
        yield item

































