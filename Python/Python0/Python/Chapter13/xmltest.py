import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter file:")
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_58931.xml"
uh = urllib.request.urlopen(url)
data=uh.read()

tree=ET.fromstring(data)
counts = tree.findall('.//count')
print("counts: ",len(counts))
sum=0
for item in counts:
    #print(item.text)
    sum=sum+int(item.text)
print('Sum: ',sum)
