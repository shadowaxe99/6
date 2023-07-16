```python
import scrapy
from web_scraper.items import QuizlitItem

class QuizlitSpider(scrapy.Spider):
    name = 'quizlit'
    allowed_domains = ['quizlit.com']
    start_urls = ['http://quizlit.com/']

    def parse(self, response):
        for post in response.css('div.post'):
            item = QuizlitItem()
            item['title'] = post.css('h2.title a::text').get()
            item['url'] = post.css('h2.title a::attr(href)').get()
            item['description'] = post.css('div.description::text').get()
            yield item

        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```