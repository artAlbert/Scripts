import requests
from bs4 import BeautifulSoup

URL = "https://environicsanalytics.com/en-ca/about/careers"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_=".d-none")
print("---------------Links-------------------")
for listing in results.find_all('div'):
    #print(listing['h3'])
    print(listing['p'])
    print(listing['href'])

#print(results.prettify())