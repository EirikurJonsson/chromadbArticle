import scrapy
from scrapy_playwright.page import PageMethod


class TV2SPIDER(scrapy.Spider):
    name = "tv2Spider"

    def start_requests(self):
        url = 'https://fyens.dk/senestenyt'
        add_url = 'https://fyens.dk/'

        yield scrapy.Request(
                url, 
                meta = {
                    'playwright': True,
                    'playwright_include_page': True,
                    'playwright_page_coroutines':[
                        PageMethod('wait_for_load_state', 'domcontentloaded')
                        ]
                    }
                )

    def parse(self, response):
        lstItem = response.css('li.list__item')
        for link in links:
            yield response.follow(f'{add_url}{link}', callback = self.parse_link)

    def parse_link(self. response):

