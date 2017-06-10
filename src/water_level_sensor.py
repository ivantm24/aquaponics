# About: This code will detect if the water in each tank
# has gone higher than the water level sensor.
# When plunger is down (water is low) the sensor reads high
# When the plunger is up (water is high) the sensor reads low

import aquaponics_gpio as agpio

class fishes_tank:

    @staticmethod
    def overflowing():
        if GPIO.input(FISHES_TANK_PIN) == 0:
            return True
        else:
            return False

class plants_left:

    @staticmethod
    def overflowing():
        if GPIO.input(PLANTS_TANK_LEFT_PIN) == 0:
            return True
        else:
            return False

class plants_right:

    @staticmethod
    def overflowing():
        if GPIO.input(PLANTS_TANK_RIGHT_PIN) == 0:
            return True
        else:
            return False