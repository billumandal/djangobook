from django.http import HttpResponse

def home(request):
	return HttpResponse("You're in the home of my django book app.")

def hello(request):
	return HttpResponse("Hello World!")