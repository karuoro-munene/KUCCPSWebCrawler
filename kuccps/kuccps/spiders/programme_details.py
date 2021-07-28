import scrapy
import json
from ..items import KuccpsItem


class ScrapeTableSpider(scrapy.Spider):
    name = 'programme_details'
    allowed_domains = ['https://students.kuccps.net/programmes/detail']
    start_urls = ['https://students.kuccps.net/programmes/detail/']

    def start_requests(self):

        with open('degree_links.json', mode='r') as f:
            json_data = json.load(f)
        urls = ['https://students.kuccps.net' + json_dict['Link'] for json_dict in json_data]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        degree = response.xpath('//*[@id="page-wrapper"]/div/div[3]/div[1]/div/h3/text()').extract_first()
        minimum_entry_requirements = {}
        for row in response.xpath('//*[@id="progDetails"]/div[1]/table/tbody/tr'):
            if row.xpath('th//text()').extract() != []:
                minimum_entry_requirements[row.xpath('th//text()').extract_first()] = row.xpath(
                    'td//text()').extract_first()
        minimum_subject_requirements = {}
        for row in response.xpath('//*[@id="progDetails"]/div[2]/table/tbody/tr'):
            minimum_subject_requirements[row.xpath('th//text()').extract_first()] = {
                row.xpath('td[1]//text()').extract_first(): row.xpath('td[2]//text()').extract_first()}
        programmes = {}
        for row in response.xpath('//*[@id="page-wrapper"]/div/div[3]/div[1]/div/div[3]/table/tbody/tr'):
            programmes[row.xpath('td[1]/a/@data-content').extract_first()] = row.xpath('td[3]/text()').extract_first()

        details = KuccpsItem()

        details['degree'] = degree
        details['minimum_entry_requirements'] = minimum_entry_requirements
        details['minimum_subject_requirements'] = minimum_subject_requirements
        details['programmes'] = programmes

        yield details
