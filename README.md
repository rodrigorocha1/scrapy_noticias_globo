# Web Scraping de Notícias do G1 com Scrapy

## Introdução

Este projeto tem como objetivo a construção de um web scraping utilizando o Scrapy para extrair informações do site [G1](https://g1.globo.com/dynamo/sp/ribeirao-preto-franca/rss2.xml) e salvar os dados em um arquivo XLSX. O arquivo XLSX será construído com as seguintes colunas:

- **TITULO**
- **SUBTITULO**
- **DESCRICAO**
- **LINK**
- **DATA_PUBLICACAO**
- **AUTOR_REPORTAGEM**
- **TEXTO_NOTICA**

## Estrutura do Web Scraping

### 1. Entrar no Site

Acesse o feed RSS das notícias em [https://g1.globo.com/dynamo/sp/ribeirao-preto-franca/rss2.xml](https://g1.globo.com/dynamo/sp/ribeirao-preto-franca/rss2.xml).

### 2. Obter Dados

Extraia as seguintes informações:
- **TÍTULOS**
- **SUBTÍTULOS**
- **DESCRIÇÕES**
- **LINKS**
- **DATA DE PUBLICAÇÃO**
- **AUTOR DA REPORTAGEM**

### 3. Acessar o Site da Notícia

Visite o link da notícia para obter informações detalhadas. Exemplo de URL: [https://g1.globo.com/sp/ribeirao-preto-franca/noticia/2024/08/22/justica-decreta-prisao-de-morador-de-rua-que-espancou-idoso-em-sertaozinho-sp.ghtml](https://g1.globo.com/sp/ribeirao-preto-franca/noticia/2024/08/22/justica-decreta-prisao-de-morador-de-rua-que-espancou-idoso-em-sertaozinho-sp.ghtml).

### 4. Obter o Autor da Notícia

Recupere o autor da notícia diretamente da página da notícia.

### 5. Obter o Texto da Notícia

Extraia o texto completo da notícia da página.

### 6. Tratamento de Dados

Realize o tratamento dos dados, incluindo:
- **Tratamento de Espaços**
- **Remoção de Tags Desnecessárias**

### 7. Salvar em Planilha XLSX

Armazene as informações extraídas em um arquivo XLSX com as colunas especificadas.

## Demonstração do Web Scraping

Para visualizar uma demonstração do web scraping, confira o código-fonte no [GitHub](https://github.com/rodrigorocha1/scrapy_noticias_globo).
Confir
Assista ao vídeo com a demonstração do projeto em [YouTube - Extração de noticias do G1 com python e Scrapy](https://youtu.be/DsCQ1fLuJ2U).


## Requisitos

- Python 3.10
- Scrapy
- pandas
- openpyxl

## Como Rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/rodrigorocha1/scrapy_noticias_globo.git
