import scrapy


class KuccpsItem(scrapy.Item):
    degree = scrapy.Field()
    minimum_entry_requirements = scrapy.Field()
    minimum_subject_requirements = scrapy.Field()
    programmes = scrapy.Field()

