from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	wcount = 0
	for word in user_text.split(' '):
		wcount +=1

	return render(request, 'reverse.html', {"reversedtext":\
		reversed_text,"userstext":user_text,"counts":wcount})
