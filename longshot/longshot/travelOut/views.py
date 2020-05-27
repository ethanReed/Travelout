from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse('<h1> TravelOut </h1?> ')

def about(request):
    return HttpResponse('<h1> TravelOut About </h1>')


# Create your views here.
