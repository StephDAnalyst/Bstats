# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BstatsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class BstatsItem(scrapy.Item):
    rank = scrapy.Field()
    player_name = scrapy.Field()
    team = scrapy.Field()
    games_played = scrapy.Field()
    minutes_per_game = scrapy.Field()
    field_goal_percentage = scrapy.Field()
    free_throw_percentage = scrapy.Field()
    three_point_field_goals_made = scrapy.Field()
    rebounds_per_game = scrapy.Field()
    assists_per_game = scrapy.Field()
    steals_per_game = scrapy.Field()
    blocks_per_game = scrapy.Field()
    turnovers_per_game = scrapy.Field()
    points_per_game = scrapy.Field()
    espn_rating = scrapy.Field()
