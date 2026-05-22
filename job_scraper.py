import requests
from bs4 import BeautifulSoup
import csv

URL = "https://realpython.github.io/fake-jobs/"

response = requests.get(URL)

if response.status_code != 200:
    print("Failed to access website")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

with open("jobs.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Title", "Company", "Location", "URL"])

    for job in jobs:

        title_tag = job.find("h2", class_="title")
        title = title_tag.text.strip() if title_tag else "N/A"

        company_tag = job.find("h3", class_="company")
        company = company_tag.text.strip() if company_tag else "N/A"

        location_tag = job.find("p", class_="location")
        location = location_tag.text.strip() if location_tag else "N/A"

        link_tag = job.find("a")
        job_url = link_tag["href"] if link_tag and link_tag.get("href") else "N/A"

        writer.writerow([title, company, location, job_url])

print("Scraping completed!")
print("Saved to jobs.csv")