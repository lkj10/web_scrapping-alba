import csv
import requests
from bs4 import BeautifulSoup

alba_url = "http://www.alba.co.kr"

site_list = []
dict = {}

codes_request = requests.get(alba_url)
codes_soup = BeautifulSoup(codes_request.text, "html.parser")

tables = codes_soup.find("div", {"id": "MainSuperBrand"})

product_tag_ul = tables.find('ul', {"class": "goodsBox"})


product_tag_li = product_tag_ul.find_all(
    'a', {"class": "goodsBox-info"})


for a in product_tag_li:
    table = a.find("span", {"class": "company"})
    try:
        file = open(f"{table.string}.csv", mode="w",
                    encoding='utf-8-sig', newline='')
        writer = csv.writer(file)
        writer.writerow(["place", "title", "time", "pay", "date"])
    except:
        pass

    site = a.attrs['href']
    site_request = requests.get(site)
    site_soup = BeautifulSoup(site_request.text, "html.parser")
    div = site_soup.find("div", {"class": "goodsList goodsJob"})
    table_tbody = div.find("table").find("tbody")
    place = table_tbody.find_all("td", {"class": "local first"})
    title = table_tbody.find_all("td", {"class": "title"})
    time = table_tbody.find_all("td", {"class": "data"})
    pay = table_tbody.find_all("td", {"class": "pay"})
    date = table_tbody.find_all("td", {"class": "regDate last"})

    for i in range(len(place)):
        dict['place'] = place[i].text
        dict['title'] = (title[i].find(
            "span", {"class": "company"})).string
        dict['time'] = time[i].string
        dict['pay'] = pay[i].text
        dict['date'] = date[i].text
        writer.writerow(list(dict.values()))
    dict = {}
print("완료")
