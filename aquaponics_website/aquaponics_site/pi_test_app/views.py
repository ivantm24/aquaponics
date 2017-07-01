from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from RPi import GPIO


def update_pin(request):
    pin = request.GET.get("pin")
    value = request.GET.get("value")
    if value is not None:
        value = value.upper().strip()
    updated = False
    message = ""

    if hasattr(GPIO,"TestMode"):
        if pin not in GPIO.PINS:
            updated = False
            message = "This PIN is not declared"
        elif value is None:
            updated = False
            value = GPIO.PINS[pin]
        elif value not in ("1", "TRUE", "0", "FALSE"):
            updated = False
            message = "Invalid value"
        else:
            updated = True
            GPIO.PINS[pin] = (value in ("1", "TRUE"))
    else:
        updated = False
        message = "GPIO is not in test mode"

    data = {
        "updated": updated,
        "pin": pin,
        "value": GPIO.PINS[pin],
        "message": message
            }
    return JsonResponse(data)