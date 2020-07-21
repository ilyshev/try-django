from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(*args, **kwargs)
	print(request.user)
	return render(request, 'home.html', {})
	# return HttpResponse("<h1>Hello world</h1>")

def contact_view(request, *args, **kwargs):
	return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
	my_context = {
		'title': 'This is about us',
		'my_number': 123,
		'this_is_true': True,
		'my_list': [123, 4564, 312, 993, 'abc'],
		'my_html': '<h1>Hello World</h1>',
	}
	return render(request, 'about.html', my_context)