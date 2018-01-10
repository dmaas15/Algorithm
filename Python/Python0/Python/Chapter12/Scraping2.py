import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

#example http://www.yahoo.com for input

url = input("Enter file:")
pos=int(input("Enter Position:"))
count=int(input("Enter Repeat Times:"))
cpos=1
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/known_by_Simah.html"

for iIndex in range(0, count):
    html=urllib.request.urlopen(url, context=ctx).read()
    soup=BeautifulSoup(html, 'html.parser')
    tags=soup('a')
    for tag in tags:
        if cpos!=pos:
            cpos=cpos+1
            continue
        #print(tag.get('href', None))
        url=tag.get('href', None)
        print(url)
        #print(cpos)
        break
    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    cpos=1
