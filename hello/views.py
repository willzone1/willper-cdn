from django.shortcuts import render
from django.http import HttpResponse
from django.template import  RequestContext
from django.shortcuts import render_to_response
import Willmain
from .models import Greeting

# Create your views here.
def index(request):
	# return HttpResponse('Hello from Python!')
	IP = get_client_ip(request)
	print(IP)
	
	# RUN CDN LOGIC HERE
	Willmain.main(IP)
	
	# Display redirect page
	return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
