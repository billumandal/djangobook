from.django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'jon.peetarson@gmail.com'),
				['billu.mandal@gmail.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')

	else:
		form = ContactForm(
			initial = {'subject': 'This is supposed to be a GMAIL test.'}
		)

	return render(request, 'contact_form.html', {'form': form})