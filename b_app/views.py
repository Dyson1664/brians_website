from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse('HIYA')


def contact(request):
    return HttpResponse('CALL ME')


# Create your views here.
