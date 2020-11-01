from django.shortcuts import render, HttpResponse

# Create your views here.
def index(repuest):
    return HttpResponse('Can you see me Now?!')
