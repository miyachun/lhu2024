#https://opendata.cwa.gov.tw/dist/opendata-swagger.html
import json,urllib.request

API_KEY='XXXX'
url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-007?Authorization='+API_KEY

data = urllib.request.urlopen(url).read()
output = json.loads(data)
location=output['records']['locations'][0]['location']


for i in location:
    print(f'{i}')


for i in location:
  name = i['locationName']
  lat=i['lat']
  print(name,lat)