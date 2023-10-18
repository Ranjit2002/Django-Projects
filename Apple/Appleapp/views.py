from django.shortcuts import render

# Create your views here.

def firstpage(request):
    return render(request, 'first.html')

def secondpage(request):
    return render(request, 'second.html')

def thirdpage(request):
    return render(request, 'third.html')

def fourthpage(request):
    return render(request, 'fourth.html')
