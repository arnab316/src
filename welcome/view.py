from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request, *args ,**kwargs):
    # return HttpResponse("<h1>Hello, world. You're at the home page.</h1>")
    return render(request, 'home.html')