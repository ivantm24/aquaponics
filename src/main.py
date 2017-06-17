import water_level_sensor as wls
import pump_controller as pump
import notifications as ntf
from aquaponics_gpio import initialize_GPIO

initialize_GPIO()

fish_tank_notification_sent = False
plant_tank_notification_sent = False

while True:
    if wls.fishes_tank.overflowing():
        if not fish_tank_notification_sent:
            print("Fish tank overflowing")
            fish_tank_notification_sent = True
    else:
        fish_tank_notification_sent = False
        if fish_tank_notification_sent:
            print("Fish tank is not longer overflowing")

    if wls.plants_left.overflowing():
        print("Left plant tank overflowing")
#        if pump.is_on():
 #           ntf.send("ALERT!!! - Aquaponics", "Plants ")           NOTE:: uncomment when adding notifications
 #       pump.turn_off()

    if wls.plants_right.overflowing():
        print("Right plant tank overflowing")