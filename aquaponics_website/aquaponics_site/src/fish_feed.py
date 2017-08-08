from . import fish_feeder

from time import gmtime, strftime
import os

path = "/home/pi/Desktop/"
if not os.path.exists(path):
    path = "/Users/ivantactukmercado/Desktop/"
filename = path+ "aquaponics_log.txt"

if os.path.exists(filename):
    append_write = 'a' # append if already exists
else:
    append_write = 'w' # make a new file if not

fish_feeder.turn_on()

with open(filename, append_write) as f:
    f.write("Fish Feeder was activated at " + strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) +"\n")

