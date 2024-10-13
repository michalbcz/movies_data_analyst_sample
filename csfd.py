import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import json

# URL of the page to scrape
url = "https://www.csfd.cz/film/12861-udoli-stinu/prehled/" # url you get when you open the movie page on csfd.cz

# We need to send a User-Agent header to pretend we are a browser (otherwise the server will block our request)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "TE": "Trailers"
}

# Send a GET request to fetch the page content
response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

# Scrape the title from the page (more resilient selector)
title_tag = soup.select_one('h1')
title = title_tag.text.strip() if title_tag else None

# Scrape the director (Režie)
reziser_section = soup.find('h4', string="Režie:")
reziser = reziser_section.find_next('a').text.strip() if reziser_section else None

# Scrape the source material (Předloha)
predloha_section = soup.find('h4', string="Předloha:")
predloha = predloha_section.find_next('a').text.strip() if predloha_section else None

# Scrape the source material type (kniha)
predloha_type_section = predloha_section.find_next('span').text.strip() if predloha_section else None

# Scrape the actors (Herci)
herci_section = soup.find('h4', string="Hrají:")
herci = []
if herci_section:
    actor_links = herci_section.find_next_siblings('a')
    for actor in actor_links:
        actor_name = actor.text.strip()
        actor_url = "https://www.csfd.cz" + actor['href']
        herci.append({"name": actor_name, "url": actor_url})

# Create the result dictionary
result = {
    "title": title,
    "reziser": reziser,
    "predloha": predloha,
    "predloha_type": predloha_type_section,
    "herci": herci
}

# Convert the result to JSON format and print it
print(json.dumps(result, indent=4, ensure_ascii=False))
