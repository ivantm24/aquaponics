import RPi.GPIO as GPIO

PUMP_SIGNAL_PIN = 3

FISHES_TANK_MIN_PIN = 4
FISHES_TANK_MAX_PIN = 5

PLANTS_TANK_MIN_PIN = 6
PLANTS_TANK_MAX_PIN = 7

TEMPERTURE = ""

GPIO_MODE = GPIO.BOARD


def initialize():
    GPIO.setmode(GPIO_MODE)

    try:
        GPIO.setup(FISHES_TANK_MIN_PIN, GPIO.IN)
    except NameError:
        print "Error defining: FISHES_TANK_MIN_PIN"

    try:
        GPIO.setup(FISHES_TANK_MAX_PIN, GPIO.IN)
    except NameError:
        print "Error defining: FISHES_TANK_MAX_PIN"

    try:
        GPIO.setup(PLANTS_TANK_MIN_PIN, GPIO.IN)
    except NameError:
        print "Error defining: PLANTS_TANK_MIN_PIN"

    try:
        GPIO.setup(PLANTS_TANK_MAX_PIN, GPIO.IN)
    except NameError:
        print "Error defining: PLANTS_TANK_MAX_PIN"

    try:
        GPIO.setup(PUMP_SIGNAL_PIN, GPIO.OUT)
    except NameError:
        print "Error defining: PUMP_SIGNAL_PIN"


initialize()