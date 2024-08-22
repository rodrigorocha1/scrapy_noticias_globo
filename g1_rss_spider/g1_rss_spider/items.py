# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class G1RssSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    descricao = scrapy.Field()
    link = scrapy.Field()
    data_publicacao = scrapy.Field()
    autor_reportagem = scrapy.Field()
