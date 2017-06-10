# Note: When plunger is down the sensor reads high
# When the plunger is up the sensor reads low

import aquaponics_gpio as agpio

class fishes_tank:

    @staticmethod
    def overflowing():
        if GPIO.input(FISHES_TANK_PIN) == 0:                #NOTE:: Need to verify functionality
            return True
        else:
            return False

    @staticmethod
    def lacking_water():
        return False


class plants_tank:

    @staticmethod
    def overflowing():
        return False

    @staticmethod
    def lacking_water():
        return False