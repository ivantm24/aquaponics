#import src.aquaponics_gpio as agpio
import RPi.GPIO as GPIO
import _thread as thread
import time

_is_on = True

def initialize(frequency=50):
    global pwm
    GPIO.setup(11, GPIO.OUT)
    pwm = GPIO.PWM(11, frequency)

def is_on():
    return _is_on

def feed(duty_cycle=5, duration=1):
    '''
    activates fish feeder and then turns it off
    :param duty_cycle: controls the speed of the motor
    :param duration: duration of the motor
    :return: 
    '''
    thread.start_new_thread(_feed_sync,(duty_cycle,duration))

def _feed_sync(duty_cycle, duration):
    turn_on(duty_cycle)
    time.sleep(duration)
    turn_off()


def turn_on(duty_cycle=None):
    global pwm, _is_on
    _is_on = True
    pwm.start(duty_cycle)


def turn_off():
    global pwm, _is_on
    _is_on = False
    pwm.stop()