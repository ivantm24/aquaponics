import threading

from django.apps import AppConfig

from aquaponics_website.aquaponics_site.src import aquaponics_system


class AquaponicsAppConfig(AppConfig):
    name = 'aquaponics_app'

    def ready(self):
        t = threading.Thread(target=aquaponics_system.main_loop)
        t.start()
