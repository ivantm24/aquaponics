from django.apps import AppConfig


class PiTestAppConfig(AppConfig):
    name = 'pi_test_app'
    def ready(self):
        global aquaponic_system
        aquaponic_system = "ak"
        print ("ready222")