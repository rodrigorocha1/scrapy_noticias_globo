# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from g1_rss_spider.items import G1RssSpiderItem
from openpyxl.styles import Font, Alignment
from scrapy.spiders import Spider
import re
from openpyxl import Workbook
from g1_rss_spider.items import G1RssSpiderItem


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


class XLSXPipeline:
    def __init__(self) -> None:
        self.workbook = Workbook()
        self.sheet = self.workbook.active

        self.sheet.title = 'Dados Coletados'
        self.sheet.append(['TITULO', 'SUBTITULO', 'DESCRICAO', 'LINK',
                          'DATA_PUBLICACAO', 'AUTOR_REPORTAGEM', 'TEXTO_NOTICA'])
        self.__aplicar_formatacao()

    def process_item(self, item: G1RssSpiderItem, spider: Spider) -> G1RssSpiderItem:
        self.gerar_dados(item)
        self._ajustar_comprimento_colunas()
        return item

    def __aplicar_formatacao(self):
        fonte_neegrito = Font(bold=True)
        alinhameto_celula = Alignment(horizontal="center")
        for cell in self.sheet["1:1"]:
            cell.font = fonte_neegrito
            cell.alignment = alinhameto_celula

    def gerar_dados(self, item: G1RssSpiderItem):
        linha = [
            item['titulo'],
            item['subtitulo'],
            item['descricao'],
            item['link'],
            item['data_publicacao'],
            item['autor_reportagem'],
            item['texto_noticia']
        ]
        self.sheet.append(linha)

    def _ajustar_comprimento_colunas(self):

        for coluna in self.sheet.columns:
            comprimento_maximo = 0
            letra_coluna = coluna[0].column_letter
            for cell in coluna:
                try:

                    comprimento_maximo = max(
                        comprimento_maximo, len(str(cell.value)))
                except:
                    pass

            comprimento_ajustado = comprimento_maximo + 2
            self.sheet.column_dimensions[letra_coluna].width = comprimento_ajustado

    def close_spider(self, spider: Spider):
        self.workbook.save('noticias.xlsx')
