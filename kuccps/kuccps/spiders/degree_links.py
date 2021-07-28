import scrapy


class ScrapeTableSpider(scrapy.Spider):
    name = 'degrees-table'
    allowed_domains = ['https://students.kuccps.net/programmes']
    start_urls = ['https://students.kuccps.net/programmes/']

    def start_requests(self):
        urls = [
            'https://students.kuccps.net/programmes/search/?group=cluster_2',
            'https://students.kuccps.net/programmes/search/?group=cluster_3',
            'https://students.kuccps.net/programmes/search/?group=cluster_4',
            'https://students.kuccps.net/programmes/search/?group=cluster_7',
            'https://students.kuccps.net/programmes/search/?group=cluster_8',
            'https://students.kuccps.net/programmes/search/?group=cluster_9',
            'https://students.kuccps.net/programmes/search/?group=cluster_10',
            'https://students.kuccps.net/programmes/search/?group=cluster_11',
            'https://students.kuccps.net/programmes/search/?group=cluster_12',
            'https://students.kuccps.net/programmes/search/?group=cluster_13',
            'https://students.kuccps.net/programmes/search/?group=cluster_15',
            'https://students.kuccps.net/programmes/search/?group=cluster_17',
            'https://students.kuccps.net/programmes/search/?group=cluster_19',
            'https://students.kuccps.net/programmes/search/?group=cluster_20',
            'https://students.kuccps.net/programmes/search/?group=cluster_21',
            'https://students.kuccps.net/programmes/search/?group=cluster_22',
            'https://students.kuccps.net/programmes/search/?group=cluster_23',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//*[@id="page-wrapper"]/div/div[3]/table/tbody/tr'):
            yield {
                'Degree': row.xpath('td[2]//text()').extract_first(),
                'Link': row.xpath('@data-href').extract_first()
            }