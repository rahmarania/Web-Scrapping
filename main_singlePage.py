import requests
from bs4 import BeautifulSoup
import csv

response = response.get("weblink.com")
soup = BeautifulSoup(response.text, 'html.parser')

# print(response.status_code)
# print(response.text)

country_blocks = soup.find_all("div", class_ = "col-md-4 country")
# print("Number of country found" (len(country_blocks))")

# get data from elemen web
res = []
for block in country_blocks:
  name_element = block.find("h3", class_ = "country-name")
  country_name = name_element.get_text(strip = True))

  capital_element = block.find("span", class_ = "country-capital")
  capital_name = capital_element.get_text(strip = True))

  population_element = block.find("span", class_ = "country-population")
  population_count = population_element.get_text(strip = True))

  area_element = block.find("span", class_ = "country-area")
  area_total = area_element.get_text(strip = True))

  result.append({"name":country_name,"capital":capital_name,"population":population_count,"area":area_total})

# check if data fetched successfully
# for item in res:
#   print(f"country: {item['name']} \n
#           capital: {item['capital']} \n
#           population: {item['population']} \n
#           area: {item['area']}")


# extract
with open("countries.csv","w",newline = "", encoding = "utf-8") as csvfile:
  fieldnames = ["name","capital","population","area"]
  writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
  writer.writeheader()
  for item item in res:
    writer.writerow(item)
