import requests
from bs4 import BeautifulSoup
import csv

# change the page_num to get another page of data
# response = request.get('https://www.scrapethissite.com/pages/forms/?page_num=15')

# create dynamic page number
BASE_URL = 'https://www.scrapethissite.com/pages/forms/'
page_num = 1
res = []

while True:
  url = f"{BASE_URL}?page_num={page_num}"
  print(f"Fetching page {url}...")
  
  response = requests.get(url)
  if response.status_code != 200:
    print(f"Failed to retrieve page {url}")
    break
  
  soup = BeautifulSoup(response.text,"html.parser")
  table = soup.find('table',class_ = "table"
  rows = table.find_all("tr", class_ = "team")

  # if the page has no data
  if not rows:
    print(f"No data found on this page: {page_num}") 
    break 
  
  for row in rows:
    team_name = row.find("id", class_ = "name").get_text(strip = True)
    year = row.find("id", class_ = "year").get_text(strip = True)
    win_rate = row.find("id", class_ = "pct").get_text(strip = True)

  res.append(["team_name":team_name,
              "year":year,
              "win_percentage":win_rate])
  
  page_num += 1



