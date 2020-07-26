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
  print(pages)



def get_jobs():
  last_page = get_last_page()
  return[]
  

