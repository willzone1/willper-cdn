#!/usr/bin/env python
import cgitb
import random
#import YourFormProcessor
import django
import geoip2.database
import httplib

#gitb.enable() # Will catch tracebacks and errors for you. Comment it out if you no-longer need it.
def main(request):
	
	willzoneConn = httplib.HTTPSConnection("willzone.zerothebeagle.dog", timeout=1)
	try:
		willzoneConn.request("HEAD","/")
		willzoneResponse = willzoneConn.getresponse()
		willzoneResponseString = willzoneResponse.reason
	except:
		print("WILLZONE down")
		willzoneResponseString = ""
	
	ravenConn = httplib.HTTPSConnection("raven.zerothebeagle.dog", timeout=1)
	try:
		ravenConn.request("HEAD","/")
		ravenResponse = ravenConn.getresponse()
		ravenResponseString = ravenResponse.reason
	except:
		print("RAVEN down")
		ravenResponseString = ""
	
	if (willzoneResponseString != "OK"):
		# choose RAVEN (1)
		serverChoice = 1
	elif (ravenResponseString != "OK"):
		# choose WILLZONE (0)
		serverChoice = 0
	else:
		IP = get_client_ip(request)
		reader = geoip2.database.Reader('GeoLite2-City.mmdb')
		# IP = "173.48.96.93"
		if IP == "127.0.0.1":
			IP = "173.48.96.93"
		response = reader.city(IP)
		latitude = response.location.latitude
		longitude = response.location.longitude
		print(latitude,longitude)
		
		# if 30 < latitude < 100, route to WILLZONE(0)
		# else RAVEN(1)
		
		if (longitude > -100 and longitude < -30):
			serverChoice = 0
		else:
			serverChoice = 1
	
	return serverChoice
	
if __name__ == '__main__':
	main()
	
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip