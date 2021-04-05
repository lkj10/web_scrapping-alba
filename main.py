import csv
import requests
from bs4 import BeautifulSoup
from save_to_file import save_to_file

alba_url = "http://www.alba.co.kr"

site_list = []
dict = {}

codes_request = requests.get(alba_url)
codes_soup = BeautifulSoup(codes_request.text, "html.parser")

tables = codes_soup.find("div", {"class": "goodsLogo goodsMain"})

product_tag_ul = tables.find('ul', {"class": "goodsBox"})

product_tag_li = product_tag_ul.find_all('li')

for i in product_tag_li:
    temp = i.find('a')['href']
    if temp[-4:] == 'MAIN':
        site_list.append(f"{alba_url}{i.find('a')['href']}")


companys = tables.find_all("span", {"class": "company"})

for company in companys:
    try:
        file = open(f"{company.string}.csv", mode="w", encoding='utf-8')
        writer = csv.writer(file)
        writer.writerow(["place", "title", "time", "pay", "date"])
    except:
        pass

for site in site_list:
    codes_request = requests.get(site)
    codes_soup = BeautifulSoup(codes_request.text, "html.parser")
    div = codes_soup.find(
        "div", {"class": "goodsList detailViewList curation detail-list--likeCorp"})
    place = div.find("table").find("tbody").find_all(
        "td", {"class": "local first"})
    title = div.find("table").find("tbody").find_all(
        "td", {"class": "title"})
    time = div.find("table").find("tbody").find_all(
        "td", {"class": "time"})
    pay = div.find("table").find("tbody").find_all(
        "td", {"class": "pay"})
    date = div.find("table").find("tbody").find_all(
        "td", {"class": "date"})
    dict['place'] = place
    dict['title'] = title
    dict['time'] = time
    dict['pay'] = pay
    dict['date'] = date
    for dic in dict:
        writer.writerow(list(dict.values()))
