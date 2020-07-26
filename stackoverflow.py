import requests
from bs4 import BeautifulSoup

url = f"https://stackoverflow.com/jobs?q=python&pg=i"

#step1; get the PAGE
#step2; make a request
#step3; extract the jobs


def get_last_page():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)  #whitespace del
    return int(last_page)


def extract_job(html):
    title = html.find("h2", {"class": "fs-body3"}).find("a")["title"]
    company = html.find("h3", {
        "class": "fs-body1"
    }).find_all(
        "span", recursive=False)
    location = company[1].get_text(strip=True)
    companys = company[0].get_text(strip=True)
    job_id = html['data-jobid']

    return {
        'title': title,
        'company': company,
        'location': location,
        'apply_link': f"https://stackoverflow.com/jobs/{job_id}"
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping stackoverflow: Page: {page}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
