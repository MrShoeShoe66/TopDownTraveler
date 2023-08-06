from tools import *
from render import *
from settingsmenu import *
from version import *
from menurender import *
import time, json, sys

global currentmap
# global currentmapid
# global settings
global win
global maps
global cords

sys.stdout.write("\x1b]2;Top Down Traveler\x07")

def menu(currentmapid, settings, data):
    internalsettings = settings
    while True:
        clear()
        sys.stdout.write("\x1b]2;Top Down Traveler\x07")
        # option = input(f"""
        option = str(rendermenu("Pause Menu", '', [
            'Exit Game',
            'Settings',
            'Save Game',
            'Resume Game'
            ], 'Hit Enter to Continue', 'blue') + 1)
        if option == '1':
            clear()
            print('Thanks for playing!')
            time.sleep(1)
            json.dump({
                "maxmaps": data["maxmapid"],
                "settings": internalsettings,
                "moddedgame": data["modded"]
            }, open('data/save.dat', 'w'))
            exit(1)
        elif option == "2":
            internalsettings = settingsmenu(internalsettings)
        elif option == '3':
            json.dump({
                "maxmaps": data["maxmapid"],
                "settings": internalsettings,
                "moddedgame": data["modded"]
            }, open('data/save.dat', 'w'))
        elif option == "4":
            clear()
            break
    return internalsettings