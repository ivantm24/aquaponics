import water_level_sensor as wls
import pump_controller as pump
import notifications as ntf
from aquaponics_gpio import initialize_GPIO

initialize_GPIO()

while True:
    if wls.fishes_tank.overflowing():
        pass
    elif wls.fishes_tank.lacking_water():
        pass

    if wls.plants_tank.overflowing():
        if pump.is_on():
            ntf.send("ALERT!!! - Aquaponics", "Plants ")
        pump.turn_off()
    elif wls.plants_tank.lacking_water():
        pass