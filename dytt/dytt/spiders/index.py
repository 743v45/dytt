#coding:utf-8
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from dytt.items import dyttItem


class download(BaseSpider):
    name = 'dytturl'
    allowed_domains = ['dytt8.net','ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html'] #先爬国内电影
    

    def parse(self, response):
        items = []
        
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/table/tbody/tr/td/b/a/@href').extract()
        for site in sites:
            site = 'www.ygdy8.net' + site
            item = dyttItem()

