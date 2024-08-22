# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from g1_rss_spider.items import G1RssSpiderItem
from scrapy.spiders import Spider
import re


class CleanG1RssPipeline:
    def process_item(self, item: G1RssSpiderItem, spider: Spider):
        item['descricao'] = ''.join(re.sub(
            r'<img.*?>|<br\s*/?>', '', item['descricao'].replace('\n', ' ')).strip())
        return item
