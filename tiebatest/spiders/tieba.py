# -*- coding: utf-8 -*-
import scrapy

from urllib.parse import urlencode
from scrapy import Request,Spider
from tiebatest.items import TiebaItem

class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    base_url = 'https://tieba.baidu.com/f?'

    def start_requests(self):
        for keyword in self.settings.get('KEY'):
            data = {'kw': keyword, 'ie': 'utf-8'}
            for i in range(0, self.settings.get('PAGE')+1):
                data['pn'] = i * 50
                params = urlencode(data)
                url = self.base_url + params
                yield Request(url=url , callback=self.parse, dont_filter=True)


    def parse(self, response):
        tiezis = response.xpath('//*[@id="thread_list"]/li')
        for tiezi in tiezis:
            item = TiebaItem()
            item['title'] = ''.join(tiezi.xpath('//div/div[2]/div[1]/div[1]/a//text()').extract()).strip()
            item['writer'] = ''.join(tiezi.xpath('//div/div[2]/div[1]/div[2]/span[1]/span[1]/a//text()').extract()).strip()
            item['time'] = ''.join(tiezi.xpath('//div/div[2]/div[1]/div[2]/span[2]//text()').extract()).strip()
            item['text'] = ''.join(tiezi.xpath('//div/div[2]/div[2]/div[1]/div[1]//text()').extract()).strip()
            item['replies'] = ''.join(tiezi.xpath('//div/div[1]/span//text()').extract()).strip()
            item['replier'] = ''.join(tiezi.xpath('//div/div[2]/div[2]/div[2]/span[1]/a//text()').extract()).strip()
            yield item
