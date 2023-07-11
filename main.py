from google_search import get_base_domain
from pdf_crawler import PdfCrawler
from scrapy.crawler import CrawlerProcess
from universities import universities, departments
import pandas as pd

API_KEY = 'YOUR_API_KEY'

def main():
    base_domains = []
    for university in universities:
        for department in departments:
            base_domain = get_base_domain(university, department, API_KEY)
            base_domains.append(base_domain)

    process = CrawlerProcess()
    process.crawl(PdfCrawler, start_urls=base_domains)
    process.start()

    pdf_links = []
    for item in PdfCrawler.items:
        pdf_links.append(item['url'])

    df = pd.DataFrame(pdf_links, columns=['url'])
    df.to_csv('pdf_links.csv', index=False)

if __name__ == '__main__':
    main()
