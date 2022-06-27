import requests, bs4, datetime, csv
import pandas as pd
# https://github.com/kennethreitz/requests-html
from requests_html import HTMLSession

date = datetime.date.today()
patients = 0
url="http://anglicanchurch.net/jobs/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# page = requests.get(url, headers=headers)
# soup = bs4.BeautifulSoup(page.text,'lxml')
# print(soup)
# with open('acna.html', 'w') as f:
#     f.write(str(soup))

# myul = soup.find("ul", {"class": "job_listings"})
# class: position, location, meta, date, company. href

# Get the html stuff
session = HTMLSession()
r = session.get(url, headers=headers)
# Render with Javascript
r = r.html.render()
# Find element UL
lis = r.find('ul')
for x in lis:
    print(x)
