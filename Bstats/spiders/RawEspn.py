import scrapy

class EspndataSpider(scrapy.Spider):
    name = "RawEspn"
    allowed_domains = ["espn.com"]
    start_urls = ["https://www.espn.com/nba/seasonleaders/_/league/nba"]

    def parse(self, response):
        table = response.xpath('//table[@class="tablehead"]')
        
        rows = table.xpath('.//tr[td]')
        for row in rows[2:]:  # Skip the first two rows (table headers)
            item = {}
            item["rank"] = row.xpath('td[1]/text()').get()
            item["player_name"] = row.xpath('td[2]/a/text()').get()
            item["team"] = row.xpath('td[3]/text()').get()
            item["games_played"] = row.xpath('td[4]/text()').get()
            item["minutes_per_game"] = row.xpath('td[5]/text()').get()
            item["field_goal_percentage"] = row.xpath('td[6]/text()').get()
            item["free_throw_percentage"] = row.xpath('td[7]/text()').get()
            item["three_point_field_goals_made"] = row.xpath('td[8]/text()').get()
            item["rebounds_per_game"] = row.xpath('td[9]/text()').get()
            item["assists_per_game"] = row.xpath('td[10]/text()').get()
            item["steals_per_game"] = row.xpath('td[11]/text()').get()
            item["blocks_per_game"] = row.xpath('td[12]/text()').get()
            item["turnovers_per_game"] = row.xpath('td[13]/text()').get()
            item["points_per_game"] = row.xpath('td[14]/text()').get()
            item["espn_rating"] = row.xpath('td[15]/text()').get()    
            
            yield item

        # Navigate to the next page if "Next" button is present
        next_page_url = response.xpath('//div[@class="jcarousel-next"]/ancestor::a/@href').get()
        if next_page_url:
            next_page_full_url = response.urljoin(next_page_url)
            yield scrapy.Request(next_page_full_url, callback=self.parse)
