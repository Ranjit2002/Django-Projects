from django.shortcuts import render

# Create your views here.

def base1page(request):
    return render(request, 'base1.html')
def base2page(request):
    return render(request, 'base2.html')

def base3page(request):
    return render(request, 'base3.html')

def first(request):
    return render(request, 'first.html')
