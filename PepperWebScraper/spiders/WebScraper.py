import scrapy
import requests
import json


class PepperWebScraper(scrapy.Spider):
    name = "pepper"
    start_urls = [
        "https://www.pepper.pl/nowe"
    ]

    def __init__(self, *a, **kw):
        super(PepperWebScraper, self).__init__(*a, **kw)
        self.r = requests.get("http://worldtimeapi.org/api/ip/188.122.20.99.json")
        self.js = json.loads(self.r.content)
        self.today_day = int(self.js["datetime"][8:10]) - 2
        self.today = 'paź {}.'.format(self.today_day)

    def parse(self, response):

        for items in response.css("div.gridLayout-item.threadCardLayout--card"):
            yield {
                "hot": items.css("span.cept-vote-temp.vote-temp::text").get(),
                "text": items.css("strong.thread-title a::attr(title)").get(),
                "promo_cost": items.css("span.thread-price.text--b.vAlign--all-tt.cept-tp.size--all-l::text").get(),
                "normal_cost": items.css("span.mute--text.text--lineThrough.size--all-l::text").get(),
                "url": items.css("div.threadCardLayout--row--large.flex.boxAlign-ai--all-c.space--h-2 a::attr(href)").get(),
                "date": items.css("div.size--all-s.flex.boxAlign-jc--all-fe.flex--grow-1.overflow--hidden span.hide--toBigCards1::text").get()
            }

            next_page = response.xpath("//span//a/@href").getall()[2]

            # Saving time of our object
            time = items.css("div.size--all-s.flex.boxAlign-jc--all-fe.flex--grow-1.overflow--hidden span.hide--toBigCards1::text").get()

            if next_page is not None and time != self.today:
                yield scrapy.Request(next_page, callback=self.parse)
            else:
                yield scrapy.Request(next_page=None, callback=None)
	

# Local time from computer
'''
today_day = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%d")
'''
