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

        item['titulo'] = item['titulo'].strip()
        item['descricao'] = item['descricao'].strip()
        item['link'] = item['link'].strip()
        item['data_publicacao'] = item['data_publicacao'].strip()
        item['autor_reportagem'] = ''.join(
            texto for texto in item['autor_reportagem']).strip()
        item['texto_noticia'] = ' '.join(
            [palavra for palavra in item['texto_noticia']]).strip()
        return item
