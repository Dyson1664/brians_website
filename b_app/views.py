from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'home.html')


def contact(request):
    return HttpResponse('CALL ME')

def index(request):
    return render(request, 'index.html')
# Create your views here.
