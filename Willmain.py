#!/usr/bin/env python
import cgitb
import random
#import YourFormProcessor
import django
import geoip2.database

#gitb.enable() # Will catch tracebacks and errors for you. Comment it out if you no-longer need it.
def main(request):
	IP = get_client_ip(request)
	reader = geoip2.database.Reader('GeoLite2-City.mmdb')
	response = reader.location(IP)
	latitude = response.location.latitude
	longitude = response.location.longitude
	print(latitude,longitude)
	return
	
if __name__ == '__main__':
	main()
	
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip