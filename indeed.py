import requests
from bs4 import BeautifulSoup

indeed_url = "https://www.indeed.com/jobs?q=python&limit=50"

def extract_indeed_pages():
  indeed = requests.get(indeed_url)

  indeed_soup = BeautifulSoup(indeed.text, "html.parser")

  pagination = indeed_soup.find("div", {"class": "pagination"})

  pages = pagination.find_all('a')
  spans = []
  for page in pages[:-1]:
    spans.append(int(page.string))

  max_page = spans[-1]
  return max_page

