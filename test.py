import pandas as pd
import requests
from bs4 import BeautifulSoup

r=requests.get('http://google.com')

soup=BeautifulSoup(r.text)

print(soup.prettify())
