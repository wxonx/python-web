from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_stackoverflow_jobs


stackoverflow_jobs = get_stackoverflow_jobs()
indeed_jobs = get_indeed_jobs()

jobs = stackoverflow_jobs + indeed_jobs
print(jobs)