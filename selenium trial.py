# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime

from pymongo import MongoClient
# client = MongoClient('mongodb://@13.209.21.3', 27017)
db = client.googleSEO

driver = webdriver.Chrome('/Users/jacob/Downloads/chromedriver')
url = 'http://www.google.com'
driver.get(url)

# 페이지의 제목을 체크하여 'Google'에 제대로 접속했는지 확인한다
assert "Google" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()
#
# with open('keywords') as f:
#     for line in f:
#         keyword = line

keyword = "Strawberry Price"
elem.send_keys(keyword)
elem.submit()

html = driver.page_source
soup = BeautifulSoup(html)
rank = 1
r = soup.select('.r')
for i in r:
    url = i.a.attrs['href']
    date = datetime.today()
    seo = {
        'url': url
        'date': date
        'rank': rank
    }
    db.googleSEO.insert_one(seo)
        rank += 1

driver.close()





