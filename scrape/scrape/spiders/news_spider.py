import scrapy

class NewsWorldSpider(scrapy.Spider):
    name="news"
    start_urls=["https://www.worldometers.info/coronavirus/"]

    def parse(self,response):
        totalcases=response.css('.maincounter-number span::text')[0].get()
        deaths=response.css('.maincounter-number span::text')[1].get()
        recovered=response.css('.maincounter-number span::text')[2].get()
        
        yield{
            'Coronavirus Cases':totalcases,
            'Total deaths':deaths,
            'Total recovered':recovered
        }
        countries=('india','nepal')
        for country in countries:
            next_page="https://www.worldometers.info/coronavirus/country/"+country+"/"
            yield scrapy.Request(next_page,callback=self.parse)
