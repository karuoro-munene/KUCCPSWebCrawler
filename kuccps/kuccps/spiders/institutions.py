import scrapy


class ScrapeTableSpider(scrapy.Spider):
    name = 'institutions-table'
    allowed_domains = ['https://students.kuccps.net/institutions']
    start_urls = ['https://students.kuccps.net/institutions/']

    def start_requests(self):
        urls = [
            'https://students.kuccps.net/institutions/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//*[@id="stInsTable"]//tbody/tr'):
            yield {
                'ID': row.xpath('td[1]//text()').extract_first(),
                'key': row.xpath('td[2]//text()').extract_first(),
                'name': row.xpath('td[3]//text()').extract_first(),
                'category': row.xpath('td[4]//text()').extract_first(),
                's_type': row.xpath('td[5]//text()').extract_first(),
            }