import scrapy


class McSweeneysSpider(scrapy.Spider):
  name = 'mcsweeneys-spider'
  start_urls = ['https://www.mcsweeneys.net/columns/hungover-bear-and-friends']

  def parse(self, response):
    for link in response.css('div.articles ul li a::attr("href")'):
      yield { 'url': link.extract() }

    next_page = response.css('span.next a::attr("href")').extract_first()
    if next_page is not None:
      yield response.follow(next_page, self.parse)
