import aquaponics_gpio as agpio

class fishes_tank:

    @staticmethod
    def overflowing():
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