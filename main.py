import requests
from bs4 import BeautifulSoup

indeed = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all('a')
spans = []
for page in pages[:-1]:
    spans.append(int(page.string))

max_page = spans[-1]


for n in range(max_page):
    print(f"start={n*50}")