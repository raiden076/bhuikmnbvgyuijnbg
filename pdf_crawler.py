import scrapy

class PdfCrawler(scrapy.Spider):
    name = 'pdf_crawler'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for href in response.css('a::attr(href)'):
            url = response.urljoin(href.extract())
            if url.endswith('.pdf'):
                yield {'url': url}
