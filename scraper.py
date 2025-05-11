import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#sara page soup me formatted
soup = BeautifulSoup(page.content,"html.parser")
#(venv) $ python -i scraper.py -> to explore html through BS-REPL env

#sara resultscontiner id results me
results = soup.find(id="ResultsContainer")
#print(results.prettify())

#sara card content div job cards me
job_cards = results.find_all("div", class_="card-content")
for job_card in job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)