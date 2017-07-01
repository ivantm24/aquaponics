from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from src import aquaponics_gpio, fish_feeder


def index(request):
    print(aquaponics_gpio.GPIO_MODE)
    context = {}
    return render(request, 'aquaponics_app/index.html', context)

def fishFeederController(request, duty_cycle=None):
    print(aquaponics_gpio.GPIO_MODE)
    context = {}
    #duty_cycle = request.GET.get('duty_cycle')
    if duty_cycle is None:
        context['message'] = "Hello"
    elif duty_cycle == '0':
        context['message'] = "It has been turn off"
        fish_feeder.turn_off()
    else:
        context['message'] = "It has been turn on"
        fish_feeder.turn_on(50)

    return render(request, 'aquaponics_app/fishFeederController.html', context)

