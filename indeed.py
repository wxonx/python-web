import requests
from bs4 import BeautifulSoup

limit = 1000
url = f"https://www.indeed.com/jobs?q=python&limit={limit}"

def extract_indeed_pages():
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class": "pagination"})
  pages = pagination.find_all('a')
  spans = []
  for page in pages[:-1]:
    spans.append(int(page.string))
  max_page = spans[-1]
  return max_page


def extract_indeed_jobs(last_page):
  jobs = []
  #for page in range(last_page):
  result = requests.get(f"{url}&start={0*limit}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
  #find.all = 리스트 전부를 가져옴
  #find는 첫번째 찾은 결과를 보여줌
  for result in results:
      title = result.find("h2", {"class": "title"}).find("a")["title"]
      company  = result.find("span", {"class": "company"})
      if company.find("a") is not None:
        print(company.find("a").string)
      else:
        print(company.string)   
  return jobs

