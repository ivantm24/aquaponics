from aquaponics_website.aquaponics_site.src import aquaponics_system

if not aquaponics_system.isRunning:
    aquaponics_system.main_loop()