from django.shortcuts import render

# Create your views here.

def index(request):
    context = {} 
    return render(request, 'aquaponics_app/index.html', context) 
