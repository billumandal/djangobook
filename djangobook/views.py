from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
import datetime

def home(request):
	return HttpResponse("You're in the home of my django book app.")

def hello(request):
	return HttpResponse("Hello World!")

def current_datetime(request):
	now = datetime.datetime.now()
	t = Template('current_datetime.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)

def hours_ahead(request, ahead):
	try:
		ahead = int(ahead)
	except ValueError:
		raise Http404()

	dt = datetime.datetime.now() + datetime.timedelta(hours=ahead)
	html = """<html>
				<head><title>Future date & time</title></head>
				<body>
					In {} hours, it'll be <strong>{}/{}/{}</strong>, time <i>{}</i> hours <i>{}</i> minutes..
				</body>
			</html>""".format(ahead, dt.day, dt.month, dt.year, dt.hour, dt.minute)
	return HttpResponse(html)

def hours_behind(request, behind):
	try:
		behind = int(behind)
	except ValueError:
		raise Http404()

	dt = datetime.datetime.now() - datetime.timedelta(hours=behind)
	html = """<html>
				<head><title>Earlier date & time</title></head>
				<body>
					{} hours ago, it was {}/{}/{}, time {} hours {} minutes..
				</body>
			</html>""".format(behind, dt.day, dt.month, dt.year, dt.hour, dt.minute)
	return HttpResponse(html)