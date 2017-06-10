import water_level_sensor as wls
import pump_controller as pump
import notifications as ntf
from aquaponics_gpio import initialize_GPIO

initialize_GPIO()

while True:
    if wls.fishes_tank.overflowing():
        print("Fish tank overflowing")

    if wls.plants_left.overflowing():
        print("Left plant tank overflowing")
#        if pump.is_on():
 #           ntf.send("ALERT!!! - Aquaponics", "Plants ")           NOTE:: uncomment when adding notifications
 #       pump.turn_off()

    if wls.plants_right.overflowing():
        print("Right plant tank overflowing")