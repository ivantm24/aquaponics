

# Assign pins
from RPi import GPIO

from src import fish_feeder

PUMP_SIGNAL_PIN = 3
TEMP_PIN = 7
FISHES_TANK_PIN = 37
PLANTS_TANK_LEFT_PIN = 33
PLANTS_TANK_RIGHT_PIN = 35
FISH_FEEDER_SIGNAL_PIN = 11

GPIO_MODE = GPIO.BOARD

def initialize_GPIO():
    GPIO.setmode(GPIO_MODE)

    fish_feeder.initialize()

    try:
        GPIO.setup(PUMP_SIGNAL_PIN, GPIO.OUT)
    except NameError:
        print("Error defining: PUMP_SIGNAL_PIN")

    try:
        GPIO.setup(PUMP_SIGNAL_PIN, GPIO.OUT)
    except NameError:
        print("Error defining: PUMP_SIGNAL_PIN")
    try:
        GPIO.setup(TEMP_PIN, GPIO.IN)
    except NameError:
        print("Error defining: TEMPERATURE_PIN")

    try:
        GPIO.setup(FISHES_TANK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    except NameError:
        print("Error defining: FISHES_TANK_PIN")

    try:
        GPIO.setup(PLANTS_TANK_LEFT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    except NameError:
        print("Error defining: PLANTS_TANK_LEFT_PIN")

    try:
        GPIO.setup(PLANTS_TANK_RIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    except NameError:
        print("Error defining: PLANTS_TANK_RIGHT_PIN")

