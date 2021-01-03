import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Inca_Empire"

response = requests.get(url)

print(response.status_code)

#q = input("you ok? ")

soup = BeautifulSoup(response.content, "html.parser")

#results = soup.find(id="ResultsContainer")

#print(results.prettify())
#job_elems = results.find_all('section', class_='card-content')
#print(job_elems)

class01 = soup.find_all('h1', class_='firstHeading')

print(class01)
for klass in class01:
  print(klass)


#title = soup.find(id = "firstHeading")
#print(title.content)