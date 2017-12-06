from django.shortcuts import render
from django.http import HttpResponse
from django.template import  RequestContext
from django.shortcuts import render_to_response
import Willmain
from .models import Greeting

# Create your views here.
def index(request):
	# return HttpResponse('Hello from Python!')
	
	# RUN CDN LOGIC HERE
	serverChoice = Willmain.main(request)
	
	print("Server chosen: %d" % serverChoice)
	
	if (serverChoice == 0):
		page = "willzone.html"
	else:
		page = "raven.html"
	# Display redirect page
	return render(request, page)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})