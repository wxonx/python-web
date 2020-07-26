import requests
from bs4 import BeautifulSoup

url = f"https://stackoverflow.com/jobs?q=python&pg=i"

#step1; get the PAGE
#step2; make a request
#step3; extract the jobs

def get_last_page():
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)#whitespace del
  return int(last_page)


def extract_jobs(last_page):
  jobs =[]
  for page in range(last_page):
    result = requests.get(f"{url}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
      print(result["data-jobid"])

    



def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
  

