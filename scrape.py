#scrape all links needed 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests

#2023-2024
#standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"

#2022-2023
#standings_url = "https://fbref.com/en/comps/9/2022-2023/2022-2023-Premier-League-Stats"

#2021-2022
#standings_url = "https://fbref.com/en/comps/9/2021-2022/2021-2022-Premier-League-Stats"

#2020-2021
standings_url = "https://fbref.com/en/comps/9/2020-2021/2020-2021-Premier-League-Stats"
headers = headers = {
}

session = requests.Session()
data = session.get(standings_url, headers=headers)
soup = BeautifulSoup(data.text,features="html.parser" )
standings_table = soup.select('table.stats_table')[0]

links = [l.get("href") for l in standings_table.find_all('a')]
links = [l for l in links if '/squads/' in l]
team_urls = [f"https://fbref.com{l}" for l in links]

previous_season = soup.select("a.prev")[0].get("href")
standings_url = f"https://fbref.com{previous_season}"

print(team_urls)
print(standings_url)