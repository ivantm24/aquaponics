try:
    import fish_feeder
except:
    from aquaponics_website.aquaponics_site.src import fish_feeder

from time import gmtime, strftime
import os

filename = "/Users/ivantactukmercado/Desktop/aquaponics_log.txt"

if os.path.exists(filename):
    append_write = 'a' # append if already exists
else:
    append_write = 'w' # make a new file if not

with open(filename, append_write) as f:
    f.write("Ran at " + strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) +"\n")