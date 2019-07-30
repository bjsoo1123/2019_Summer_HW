from django.shortcuts import render

def show(request):
    
    return render(request, 'show.html')

def home(request):
    
    return render(request, 'home.html')
