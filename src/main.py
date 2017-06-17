import water_level_sensor as wls
import pump_controller as pump
import notifications as ntf
from aquaponics_gpio import initialize_GPIO

initialize_GPIO()

fish_tank_notification_sent = False
plant_tank_notification_sent = False

flags={}

def verify_send_alert(alert_method, activated_message, message_deactivate):
    if alert_method not in flags:
        flags[alert_method] = False
    if alert_method():
        if not flags[alert_method]:
            print activated_message
            flags[alert_method] = True
    else:
        if flags[alert_method]:
            print message_deactivate
        flags[alert_method] = False


while True:
    verify_send_alert(wls.fishes_tank.overflowing,"Fish tank overflowing","Fish tank is not longer overflowing")

    verify_send_alert(wls.plants_left.overflowing, "Left plant tank overflowing", "Left plant tank is not longer overflowing")

    # if wls.plants_left.overflowing():
    #     print("Left plant tank overflowing")
#        if pump.is_on():
 #           ntf.send("ALERT!!! - Aquaponics", "Plants ")           NOTE:: uncomment when adding notifications
 #       pump.turn_off()
    verify_send_alert(wls.plants_right.overflowing, "Right plant tank overflowing",
                      "Right plant tank is not longer overflowing")

