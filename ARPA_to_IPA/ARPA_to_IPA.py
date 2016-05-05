from bs4 import BeautifulSoup
import requests
import urllib3

# Sundance event URL
url = ('https://www.wikiwand.com/en/Arpabet')
http = urllib3.PoolManager()
r = http.request('GET', url)
soup = BeautifulSoup(r, "html.parser")

for table in soup.find_all('table'):
	for 
