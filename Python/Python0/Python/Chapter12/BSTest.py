import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#example http://www.yahoo.com for input
url=input('Enter - ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')

tags=soup('a')
for tag in tags:
    print(tag.get('href', None))
