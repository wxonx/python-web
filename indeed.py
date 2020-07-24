import requests
from bs4 import BeautifulSoup

limit = 500
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


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = (str(company_anchor.string))
    else:
        company = (str(company.string))
    company = company.strip()
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    print(location)
    return {'title': title, 'company': company, 'location': location}


def extract_indeed_jobs(last_page):
    jobs = []
    #for page in range(last_page):
    result = requests.get(f"{url}&start={0*limit}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    #find.all = 리스트 전부를 가져옴
    #find는 첫번째 찾은 결과를 보여줌
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs
