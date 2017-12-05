from django.shortcuts import render
from django.http import HttpResponse
import main

from .models import Greeting

# Create your views here.
def index(request):
	# return HttpResponse('Hello from Python!')
	main.main()
	return render(request, 'index.html')
	#TODO: write code that redirects


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

