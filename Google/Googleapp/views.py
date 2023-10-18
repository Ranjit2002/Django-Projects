from django.shortcuts import render

# Create your views here.

def firstpage(request):
    return render(request, 'first.html')

def secondpage(request):
    return render(request, 'second.html')
