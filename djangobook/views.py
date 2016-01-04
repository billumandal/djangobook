from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime
from books.models import Book

def home(request):
	return HttpResponse("You're in the home of my django book app.")

def hello(request):
	referrer = ''
	remote_address = ''
	try:
		ua = request.META['HTTP_USER_AGENT']
		referrer = request.META['REFERER']
		remote_address = request.META['REMOTE_ADDR']

	except KeyError:
		'Unknown ua'

	return HttpResponse("""Fuck you you fucking fucker.
		<br> Page is {}. 
		<br> Our browser {}. 
		<br> &amp; referrer is {}. 
		<br> Remote Address is {}.""".format(request.path, ua, referrer, remote_address))

def current_datetime(request):
	now = datetime.datetime.now()
	# t = Template('current_datetime.html')
	# html = t.render(Context({'current_date': now}))
	# return HttpResponse(html)
	return render(request, 'current_datetime.html', {'current_date': now})

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

def display_meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>{}</td><td>{}</td></tr>'.format(k, v))

	return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_results.html', {'books':books, 'query':q})

		return render(request, 'search_form.html', {'error':error})

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_results.html', {'books': books, 'query': q })
	
	return render(request, 'search_form.html', {'errors': errors})