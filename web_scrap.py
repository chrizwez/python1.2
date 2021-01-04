import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Inca_Empire"

response = requests.get(url)

print(response.status_code)
#print(response.content())

#q = input("you ok? ")

soup = BeautifulSoup(response.content, "html.parser")

header = soup.find(id="firstHeading")

body = soup.find_all(id='bodyContent')

bodies = soup.find_all('h3',class_='mw-headline')
sub = []
#for bod in bodies:
#  Subs = bod.find('h3', #class_='mw-headline')
#  Subs = Subs#.text
#  sub.append(Subs)

print(bodies)
#a = input("ok")
print(header.text)

#print(results.prettify())
#job_elems = results.find_all('section', class_='card-content')
#print(job_elems)

#page = results.find_all()
#class01 = soup.find_all('center')

#class02 = soup.find('h2')

#print(class02)


#print(class01)
#x = input("is this good? ")
#for klass in class01:
 # print(klass)


#title = soup.find(id = "firstHeading")
#print(title.content)