import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

address=raw_input("Enter a valid place to inquire about:")

if len(address)>0:
    url=serviceurl+urllib.urlencode({"sensor":"false","address":address})
else:
    print "**Name of a place cannot be empty string**"
    quit()

#print url

data=urllib.urlopen(url).read()

geodata=json.loads(data)

if geodata["status"]=="ZERO_RESULTS":
    print "Entered Place in invalid"

lat= geodata["results"][0]["geometry"]["location"]["lat"]
long=geodata["results"][0]["geometry"]["location"]["lng"]
type= geodata["results"][0]["types"][0]
full_address=geodata["results"][0]["formatted_address"]

print "Full Address:",full_address
print "Latitude:",lat
print "Longitude:",long
print "Type of Place:",type
