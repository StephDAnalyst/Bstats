# ESPN NBA Season Leaders Scraper with Data Validation Pipelines

This Scrapy spider scrapes data from ESPN's NBA season leaders page and extracts player statistics. It includes data validation pipelines.

## Overview

- The spider starts from the [ESPN NBA Season Leaders](https://www.espn.com/nba/seasonleaders/_/league/nba) page.
- It collects data for the top-performing NBA players during the season.
- The spider retrieves player data such as rank, player name, team, games played, minutes per game, field goal percentage, free throw percentage, three-point field goals made, rebounds per game, assists per game, steals per game, blocks per game, turnovers per game, points per game, and ESPN rating.


## Prerequisites

Before running the spider, make sure you have Scrapy installed. You can install Scrapy using pip:

```bash
pip install scrapy
```

## Usage        
To run the spider, execute the following command in the project directory:
```bash
scrapy crawl espndata -o espn_nba_season_leaders.csv
```
This command will run the spider and save the scraped data to a CSV file named espn_nba_season_leaders.csv.

## Spider Details
* Spider Name: espndata
* Allowed Domains: espn.com
* Start URLs: ESPN NBA Season Leaders

## Output

The spider generates a CSV file (espn_nba_season_leaders.csv) containing player statistics. The CSV file includes columns for each player's rank, name, team, and various performance metrics.

## Item Pipeline
The spider uses item pipelines to validate and clean the scraped data. The pipeline ensures that the extracted data conforms to the expected data types before saving it.

## Contributing

Contributions to improve this spider or add new features are welcome. Please fork the repository and submit a pull request.
