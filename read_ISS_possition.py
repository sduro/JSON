#!/usr/bin/env python3

from urllib.request import urlopen
import json
import time

feed_url="https://api.wheretheiss.at/v1/satellites/25544"

def informacion():
	try:
		jsonFeed = urlopen(feed_url)
		feedData = jsonFeed.read()
		#print feedData
		jsonFeed.close()
		data = json.loads(feedData)
		return data
	except Exception:
		import traceback
		print ("generic exception: " + traceback.format_exc())
 
	return []		
 
#use this method to retrieve from web API
def parseISSDataFeed():
	data = informacion()
	if len(data) == 0:
		return []

	name = data['name']
	lat = data['latitude']
	lng = data['longitude']
	alt = data['altitude']

	return [name, lng, lat, alt]

def main():
        print (parseISSDataFeed())

if __name__ == "__main__":
    while(1):
        time.sleep(1)
        main()

    
    
