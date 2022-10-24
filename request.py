import requests
from bs4 import BeautifulSoup

url = 'http://0.0.0.0:8000/desafio'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
stings = soup.find_all('td')
for word in stings:
    if word.text == 'Ola Mundo':
        print('Found')
    else:
        print('Not Found')


