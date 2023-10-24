from django.shortcuts import render

# Create your views here.

def base1page(request):
    return render(request, 'base1.html')

def base2page(request):
    return render(request, 'base2.html')

def firstpage(request):
    return render(request, 'first.html')
