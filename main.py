import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")

alba_url = "http://www.alba.co.kr"


codes_request = requests.get(alba_url)
codes_soup = BeautifulSoup(codes_request.text, "html.parser")

tables = codes_soup.find("div", {"class": "goodsLogo goodsMain"})
companys = tables.find_all("span", {"class": "company"})
print(companys)
# print(tables)
