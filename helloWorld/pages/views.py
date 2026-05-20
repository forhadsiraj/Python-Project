from django.shortcuts import render
from django.http import HttpResponse

def home_page_view (request):
    return HttpResponse("<h1>Hello, World!</h1>")