import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

#example http://www.yahoo.com for input

url = input("Enter file:")
if len(url) < 1 : url = "http://http://naenara.com.kp/"

html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html, 'html.parser')

tags=soup('span')
sum=0
for tag in tags:
    print("SPAN:",tag)
#    number=re.findall('[0-9]+',tag)
    print('Contents:', tag.contents[0])
    sum=sum+int(tag.contents[0])
print(sum)
