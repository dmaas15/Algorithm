import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1:
    address="http://py4e-data.dr-chuck.net/comments_58932.json"

print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)

#print(json.dumps(js, indent=4))

count=0
for item in js["comments"]:
    count=int(item['count'])+count
print(count)
