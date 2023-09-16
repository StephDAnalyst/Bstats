# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BstatsPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        ## Strip all whitespaces from strings
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name == "team"  or field_name == "player_name" :
                value = adapter.get(field_name)
                adapter[field_name] = value.strip()
        
        conversion_fields = {
            "rank": int,
            "games_played": int,
            "minutes_per_game": float,
            "field_goal_percentage": float,
            "free_throw_percentage": float,
            "three_point_field_goals_made": float,
            "rebounds_per_game": float,
            "assists_per_game": float,
            "steals_per_game": float,
            "blocks_per_game": float,
            "turnovers_per_game": float,
            "points_per_game": float,
            "espn_rating": float,
        }
        for key, data_type in conversion_fields.items():
            try:
                adapter[key] = data_type(adapter[key])
            except(ValueError, TypeError):
                pass
                                      
        return item
