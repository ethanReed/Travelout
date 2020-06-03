from django.shortcuts import render
from django.shortcuts import HttpResponse

posts = [
    {
        'author': 'jack N',
        'title': 'why you should travel',
        'content': 'article1',
        'date': 'june 19th, 2019'
    },
    {
        'author': 'jack H',
        'title': 'why you should not travel2',
        'content': 'article2',
        'date': 'june 21th, 2010',
    }
]

def home(request):
    context = {'posts':posts}
    return render(request, 'travelOut/home.html', context)

def about(request):
    return render(request, 'travelOut/about.html', {'title':about})



# Create your views here.
