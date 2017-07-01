import src.aquaponics_gpio as agpio
import RPi.GPIO as GPIO

_is_on = True

def initialize(frequency=50):
    global pwm
    GPIO.setup(agpio.FISH_FEEDER_SIGNAL_PIN, GPIO.OUT)
    pwm = GPIO.PWM(agpio.FISH_FEEDER_SIGNAL_PIN, frequency)

def is_on():
    return _is_on


def turn_on(duty_cycle=None):
    global pwm, _is_on
    _is_on = True
    pwm.start(duty_cycle)


def turn_off():
    global pwm, _is_on
    _is_on = False
    pwm.stop()