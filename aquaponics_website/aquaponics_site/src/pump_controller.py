import src.aquaponics_gpio as agpio
import RPi.GPIO as GPIO

_is_on = True


def is_on():
    return _is_on


def turn_on():
    _is_on = True
    GPIO.output(agpio.PUMP_SIGNAL_PIN, False)


def turn_off():
    _is_on = False
    GPIO.output(agpio.PUMP_SIGNAL_PIN, True)