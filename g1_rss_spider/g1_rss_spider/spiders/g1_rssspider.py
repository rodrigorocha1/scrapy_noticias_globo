import scrapy
import re
from scrapy.http import Response
from g1_rss_spider.items import G1RssSpiderItem


class G1RssspiderSpider(scrapy.Spider):
    name = "g1_rssspider"
    allowed_domains = ["g1.globo.com"]
    start_urls = [
        "https://g1.globo.com/dynamo/sp/ribeirao-preto-franca/rss2.xml"]

    def parse(self, response: Response):
        titulos = response.xpath('//item/title/text()').getall()
        descricoes = response.xpath('//item/description/text()').getall()
        links = response.xpath('//item/link/text()').getall()
        data_publicacoes = response.xpath('//item/pubDate/text()').getall()

        url_noticas = response.xpath('//item/guid/text()').getall()

        for titulo, descricao, link, data_publicacao, descricao, url in zip(titulos, descricoes, links, data_publicacoes, descricoes, url_noticas):
            yield response.follow(
                url,
                self.parse_artigo_g1, meta={
                    'titulo': titulo,
                    'descricao': descricao,
                    'link': link,
                    'data_publicacao': data_publicacao
                }
            )

    def parse_artigo_g1(self, response: Response):
        item = G1RssSpiderItem()
        item['titulo'] = response.meta['titulo'].strip()
        item['descricao'] = response.meta['descricao'].strip()
        item['link'] = response.meta['link'].strip()
        item['data_publicacao'] = response.meta['data_publicacao'].strip()
        item['autor_reportagem'] = response.xpath(
            '//p[@class="content-publication-data__from"]/text()').get()

        yield item
