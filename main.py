import requests
from bs4 import BeautifulSoup

indeed = requests.get(
    "https://www.indeed.com/jobs?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch"
)

indeed_soup = BeautifulSoup(indeed.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all('a')
spans = []
for page in pages:
    spans.append(page.find("span"))

print(spans[:-1])
