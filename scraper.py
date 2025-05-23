# import requests
# from bs4 import BeautifulSoup

# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)

# #sara page soup me formatted
# soup = BeautifulSoup(page.content,"html.parser")
# #(venv) $ python -i scraper.py -> to explore html through BS-REPL env

# #sara resultscontiner id results me
# results = soup.find(id="ResultsContainer")
# #print(results.prettify())

# #sara card content div job cards me
# job_cards = results.find_all("div", class_="card-content")
# for job_card in job_cards:
#     title_element = job_card.find("h2", class_="title")
#     company_element = job_card.find("h3", class_="company")
#     location_element = job_card.find("p", class_="location")
#     # print(title_element.text.strip())
#     # print(company_element.text.strip())
#     # print(location_element.text.strip())
#     # print()
#     # print()
#     # print()

# #sara python jobs job me
# python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
# print(len(python_jobs))

# #upper hierarchy traversal
# python_job_cards = [h2_element.parent.parent.parent for h2_element in python_jobs]

# #going down agai to fetch relevant info
# for job_card in python_job_cards:
#      title_element = job_card.find("h2", class_="title")
#      company_element = job_card.find("h3", class_="company")
#      location_element = job_card.find("p", class_="location")
#     #  print(title_element.text.strip())
#     #  print(company_element.text.strip())
#     #  print(location_element.text.strip())
#     #  print()

# #going down to get links
# for job_card in python_job_cards:
#     link_url = job_card.find_all("a")[1]["href"]
#     print(link_url)

#FINAL CODE
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_card in python_job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    link_url = job_card.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")