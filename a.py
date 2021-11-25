import requests
import os
from bs4 import BeautifulSoup
page = requests.get('https://codeforces.com/contest/1578/submission/130467899')
page=requests.get('https://codeforces.com/contest/1598/submission/131409836')
print(page.url)
# soup = BeautifulSoup(page.content, "html.parser")
# x=soup.find('html')
# x=x.find('body').find('div', id='header').find('div').find('a')['href']
# print(x)
# print(soup.prettify)