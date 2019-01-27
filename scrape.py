import requests
import random
from bs4 import BeautifulSoup

data = requests.get('https://www.billboard.com/charts/hot-100/')

soup = BeautifulSoup(data.text, 'html.parser')

text = []

for div in soup.find_all('div', {'class': 'chart-number-one__title'}):
	text.append(div.text)
for span in soup.find_all('span', {'class': 'chart-list-item__title-text'}):
	text.append(span.text)

text = [i.replace('\n','') for i in text]
text = ' '.join(text).replace(' ', '\n').replace('(', '').replace(')', '').splitlines()

for i in range(3):
	myline = random.choice(text)
	print(myline, end=' ')
