import pandas as pd
import requests


r=requests.get('http://google.com')

print(r.text)
