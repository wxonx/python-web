import requests
from bs4 import BeautifulSoup

limit = 50
url = f"https://www.indeed.com/jobs?q=python&limit={limit}"

def extract_indeed_pages():
  indeed = requests.get(url)

  indeed_soup = BeautifulSoup(indeed.text, "html.parser")

  pagination = indeed_soup.find("div", {"class": "pagination"})

  pages = pagination.find_all('a')
  spans = []
  for page in pages[:-1]:
    spans.append(int(page.string))

  max_page = spans[-1]
  return max_page


def extract_indeed_jobs(last_page):
  for page in range(last_page):
    print(f"&start={page*limit}")


