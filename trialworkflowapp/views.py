from django.shortcuts import render

# Create your views here.
def welcome(request):
    message = "Welcome to github actions trial"
    return render(request, 'welcome.html',{"message":message})
