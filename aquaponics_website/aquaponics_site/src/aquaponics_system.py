import src.water_level_sensor as wls
import src.pump_controller as pump
import src.notifications as ntf
from src.aquaponics_gpio import initialize_GPIO

initialize_GPIO()

fish_tank_notification_sent = False
plant_tank_notification_sent = False

has_been_activated={}

def verify_send_alert(alert_method, activated_message, message_deactivate):
    """
    This method verifies if an alert have been triggered and only sends a notification once.
    :param alert_method: It's a verification method for an event in the system. Should return True or False
    :param activated_message: 
    :param message_deactivate: 
    :return: 
    """
    if alert_method not in has_been_activated:
        has_been_activated[alert_method] = False  #intialize flag for that method
    if alert_method():
        if not has_been_activated[alert_method]:
            print(activated_message)
            has_been_activated[alert_method] = True
    else:
        if has_been_activated[alert_method]:
            print(message_deactivate)
        has_been_activated[alert_method] = False

isRunning = False
def main_loop():
    global isRunning
    isRunning = True
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
    isRunning = False
