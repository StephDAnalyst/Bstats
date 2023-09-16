import scrapy
from Bstats.items import BstatsItem
class EspndataSpider(scrapy.Spider):
    name = "espndata"
    allowed_domains = ["espn.com"]
    start_urls = ["https://www.espn.com/nba/seasonleaders/_/league/nba"]

    def parse(self, response):
        table = response.xpath('//table[@class="tablehead"]')
        
        rows = table.xpath('.//tr[td]')
        for row in rows[2:]:  # Skip the first two rows (table headers)
            espn_item = BstatsItem()
            espn_item["rank"] = row.xpath('td[1]/text()').get()
            espn_item["player_name"] = row.xpath('td[2]/a/text()').get()
            espn_item["team"] = row.xpath('td[3]/text()').get()
            espn_item["games_played"] = row.xpath('td[4]/text()').get()
            espn_item["minutes_per_game"] = row.xpath('td[5]/text()').get()
            espn_item["field_goal_percentage"] = row.xpath('td[6]/text()').get()
            espn_item["free_throw_percentage"] = row.xpath('td[7]/text()').get()
            espn_item["three_point_field_goals_made"] = row.xpath('td[8]/text()').get()
            espn_item["rebounds_per_game"] = row.xpath('td[9]/text()').get()
            espn_item["assists_per_game"] = row.xpath('td[10]/text()').get()
            espn_item["steals_per_game"] = row.xpath('td[11]/text()').get()
            espn_item["blocks_per_game"] = row.xpath('td[12]/text()').get()
            espn_item["turnovers_per_game"] = row.xpath('td[13]/text()').get()
            espn_item["points_per_game"] = row.xpath('td[14]/text()').get()
            espn_item["espn_rating"] = row.xpath('td[15]/text()').get()    
            
            yield espn_item

        # Navigate to the next page if "Next" button is present
        next_page_url = response.xpath('//div[@class="jcarousel-next"]/ancestor::a/@href').get()
        if next_page_url:
            next_page_full_url = response.urljoin(next_page_url)
            yield scrapy.Request(next_page_full_url, callback=self.parse)
