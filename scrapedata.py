#scrape all match data
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
#2023-2024
#team_urls = ['https://fbref.com/en/squads/361ca564/Tottenham-Hotspur-Stats', 'https://fbref.com/en/squads/18bb7c10/Arsenal-Stats', 'https://fbref.com/en/squads/b8fd03ef/Manchester-City-Stats', 'https://fbref.com/en/squads/822bd0ba/Liverpool-Stats', 'https://fbref.com/en/squads/8602292d/Aston-Villa-Stats', 'https://fbref.com/en/squads/d07537b9/Brighton-and-Hove-Albion-Stats', 'https://fbref.com/en/squads/7c21e445/West-Ham-United-Stats', 'https://fbref.com/en/squads/b2b47a98/Newcastle-United-Stats', 'https://fbref.com/en/squads/47c64c55/Crystal-Palace-Stats', 'https://fbref.com/en/squads/19538871/Manchester-United-Stats', 'https://fbref.com/en/squads/cff3d9bb/Chelsea-Stats', 'https://fbref.com/en/squads/fd962109/Fulham-Stats', 'https://fbref.com/en/squads/e4a775cb/Nottingham-Forest-Stats', 'https://fbref.com/en/squads/8cec06e1/Wolverhampton-Wanderers-Stats', 'https://fbref.com/en/squads/cd051869/Brentford-Stats', 'https://fbref.com/en/squads/d3fd31cc/Everton-Stats', 'https://fbref.com/en/squads/e297cd13/Luton-Town-Stats', 'https://fbref.com/en/squads/943e8050/Burnley-Stats', 'https://fbref.com/en/squads/4ba7cbea/Bournemouth-Stats', 'https://fbref.com/en/squads/1df6b87e/Sheffield-United-Stats']

#2022-2023
#team_urls = ['https://fbref.com/en/squads/b8fd03ef/2022-2023/Manchester-City-Stats', 'https://fbref.com/en/squads/18bb7c10/2022-2023/Arsenal-Stats', 'https://fbref.com/en/squads/19538871/2022-2023/Manchester-United-Stats', 'https://fbref.com/en/squads/b2b47a98/2022-2023/Newcastle-United-Stats', 'https://fbref.com/en/squads/822bd0ba/2022-2023/Liverpool-Stats', 'https://fbref.com/en/squads/d07537b9/2022-2023/Brighton-and-Hove-Albion-Stats', 'https://fbref.com/en/squads/8602292d/2022-2023/Aston-Villa-Stats', 'https://fbref.com/en/squads/361ca564/2022-2023/Tottenham-Hotspur-Stats', 'https://fbref.com/en/squads/cd051869/2022-2023/Brentford-Stats', 'https://fbref.com/en/squads/fd962109/2022-2023/Fulham-Stats', 'https://fbref.com/en/squads/47c64c55/2022-2023/Crystal-Palace-Stats', 'https://fbref.com/en/squads/cff3d9bb/2022-2023/Chelsea-Stats', 'https://fbref.com/en/squads/8cec06e1/2022-2023/Wolverhampton-Wanderers-Stats', 'https://fbref.com/en/squads/7c21e445/2022-2023/West-Ham-United-Stats', 'https://fbref.com/en/squads/4ba7cbea/2022-2023/Bournemouth-Stats', 'https://fbref.com/en/squads/e4a775cb/2022-2023/Nottingham-Forest-Stats', 'https://fbref.com/en/squads/d3fd31cc/2022-2023/Everton-Stats', 'https://fbref.com/en/squads/a2d435b3/2022-2023/Leicester-City-Stats', 'https://fbref.com/en/squads/5bfb9659/2022-2023/Leeds-United-Stats', 'https://fbref.com/en/squads/33c895d4/2022-2023/Southampton-Stats']

#2021-2022
#team_urls = ['https://fbref.com/en/squads/b8fd03ef/2021-2022/Manchester-City-Stats', 'https://fbref.com/en/squads/822bd0ba/2021-2022/Liverpool-Stats', 'https://fbref.com/en/squads/cff3d9bb/2021-2022/Chelsea-Stats', 'https://fbref.com/en/squads/361ca564/2021-2022/Tottenham-Hotspur-Stats', 'https://fbref.com/en/squads/18bb7c10/2021-2022/Arsenal-Stats', 'https://fbref.com/en/squads/19538871/2021-2022/Manchester-United-Stats', 'https://fbref.com/en/squads/7c21e445/2021-2022/West-Ham-United-Stats', 'https://fbref.com/en/squads/a2d435b3/2021-2022/Leicester-City-Stats', 'https://fbref.com/en/squads/d07537b9/2021-2022/Brighton-and-Hove-Albion-Stats', 'https://fbref.com/en/squads/8cec06e1/2021-2022/Wolverhampton-Wanderers-Stats', 'https://fbref.com/en/squads/b2b47a98/2021-2022/Newcastle-United-Stats', 'https://fbref.com/en/squads/47c64c55/2021-2022/Crystal-Palace-Stats', 'https://fbref.com/en/squads/cd051869/2021-2022/Brentford-Stats', 'https://fbref.com/en/squads/8602292d/2021-2022/Aston-Villa-Stats', 'https://fbref.com/en/squads/33c895d4/2021-2022/Southampton-Stats', 'https://fbref.com/en/squads/d3fd31cc/2021-2022/Everton-Stats', 'https://fbref.com/en/squads/5bfb9659/2021-2022/Leeds-United-Stats', 'https://fbref.com/en/squads/943e8050/2021-2022/Burnley-Stats', 'https://fbref.com/en/squads/2abfe087/2021-2022/Watford-Stats', 'https://fbref.com/en/squads/1c781004/2021-2022/Norwich-City-Stats']

#2020-2021
team_urls =['https://fbref.com/en/squads/b8fd03ef/2020-2021/Manchester-City-Stats', 'https://fbref.com/en/squads/19538871/2020-2021/Manchester-United-Stats', 'https://fbref.com/en/squads/822bd0ba/2020-2021/Liverpool-Stats', 'https://fbref.com/en/squads/cff3d9bb/2020-2021/Chelsea-Stats', 'https://fbref.com/en/squads/a2d435b3/2020-2021/Leicester-City-Stats', 'https://fbref.com/en/squads/7c21e445/2020-2021/West-Ham-United-Stats', 'https://fbref.com/en/squads/361ca564/2020-2021/Tottenham-Hotspur-Stats', 'https://fbref.com/en/squads/18bb7c10/2020-2021/Arsenal-Stats', 'https://fbref.com/en/squads/5bfb9659/2020-2021/Leeds-United-Stats', 'https://fbref.com/en/squads/d3fd31cc/2020-2021/Everton-Stats', 'https://fbref.com/en/squads/8602292d/2020-2021/Aston-Villa-Stats', 'https://fbref.com/en/squads/b2b47a98/2020-2021/Newcastle-United-Stats', 'https://fbref.com/en/squads/8cec06e1/2020-2021/Wolverhampton-Wanderers-Stats', 'https://fbref.com/en/squads/47c64c55/2020-2021/Crystal-Palace-Stats', 'https://fbref.com/en/squads/33c895d4/2020-2021/Southampton-Stats', 'https://fbref.com/en/squads/d07537b9/2020-2021/Brighton-and-Hove-Albion-Stats', 'https://fbref.com/en/squads/943e8050/2020-2021/Burnley-Stats', 'https://fbref.com/en/squads/fd962109/2020-2021/Fulham-Stats', 'https://fbref.com/en/squads/60c6b05f/2020-2021/West-Bromwich-Albion-Stats', 'https://fbref.com/en/squads/1df6b87e/2020-2021/Sheffield-United-Stats']

headers = headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
}

session = requests.Session()


all_matches = []
year = 2020

for team_url in team_urls:

    team_name = team_url.split("/")[-1].replace("-Stats", "").replace("-", " ")
    data = session.get(team_url, headers=headers)
    matches = pd.read_html(data.text, match="Scores & Fixtures", flavor='bs4')[0]
    soup = BeautifulSoup(data.text, features="html.parser")
    links = [l.get("href") for l in soup.find_all('a')]
    links = [l for l in links if l and 'all_comps/shooting/' in l]
    time.sleep(1)
    data = session.get(f"https://fbref.com{links[0]}", headers=headers)
    shooting = pd.read_html(data.text, match="Shooting", flavor='bs4')[0]
    shooting.columns = shooting.columns.droplevel()
    try:
        team_data = matches.merge(shooting[["Date", "Sh", "SoT", "Dist", "FK", "PK", "PKatt"]], on="Date")
    except ValueError:
        continue
    team_data = team_data[team_data["Comp"] == "Premier League"]
    
    team_data["Season"] = year
    team_data["Team"] = team_name
    all_matches.append(team_data)
    time.sleep(1)

match_df = pd.concat(all_matches)

match_df.columns = [c.lower() for c in match_df.columns]

match_df.to_csv(f"match{year}.csv")