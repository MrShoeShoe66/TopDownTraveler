import sys, json, getpass, os, mapworker

sys.stdout.write("\x1b]2;Top Down Traveler\x07")

from tools import *
from render import *
from version import *
from settingsmenu import *

global settings
global maps
global mapcount
global maxmapid
global currentmapid
global currentmap
global cords
global win
global pressed
global held

clear()

settings = {
    "color": False
}

newestkeyunhook = False

mapdat = json.load( open('data/map.dat') )

maps = mapdat['data']
mapcount = len(maps)

global modded

modded = mapdat['modded']

__mapversion__ = mapdat['mapfileversion']

__modded__ = mapdat['modded']

savedata = json.load( open('data/save.dat') )

dummysave = {"maxmaps": 0, "settings": {"color": False}, "moddedgame": False}

maxmapid = savedata['maxmaps']
currentmapid = maxmapid

if __modded__ != savedata['moddedgame']:
    if savedata['moddedgame']:
        print("Hey! this is a modded save file and a non modded game!")
    elif not savedata['moddedgame'] and savedata != dummysave:
        print('This is a modded game and a not modded save file!')
    while True:
        pass

if maxmapid == mapcount:
    print("Hey! The save file your using is completed! Thanks for playing my game!")
    currentmapid = 0

nextframeHold = False

currentmap = maps[currentmapid]['data']
cords = maps[currentmapid]['cords']['start']
win = maps[currentmapid]['cords']['end']
settings = savedata['settings']

while True:
    menuoption = str(rendermenu('--- ################################## ---\n             Top Down Traveler\n--- ################################## ---', '', 
    [
        'Play Game',
        'Settings',
        'How to play',
        'Quit',
        'Game Info'
    ], color='blue') + 1)

    if menuoption == '1':
        break
    
    if menuoption == '2':
        settings = settingsmenu(settings)
    
    if menuoption == '3':
        clear()
        getpass.getpass("""
--- ################################## ---
                How to play
--- ################################## ---

WASD  - Move / Pick Menu item
ENTER - Select menu item 
ESC   - Pause Game

""")

    if menuoption == '5':
        clear()
        getpass.getpass(f"""
--- ################################## ---
                Game Info
--- ################################## ---

Version - {version}

Map File Version - {__mapversion__}

Modded - {__modded__}

Color Mode - {settings['color']}

""")
# Debug Mode - {settings['debug']}

# """)
    
    if menuoption == '4':
        exit(1)
    
    clear()

clear()

from menu import * 

paused = False
pausedhold = False

while True:
    out = mapworker.playmap(currentmap, {
        "playercords": cords,
        'wincords': win,
        "color": settings['color'],
        'mapid': currentmapid,
        'mapcount': mapcount,
        'debug': settings['debug']
    })
    
    if out[0] == True:
        if currentmapid == mapcount-1:
            break
        currentmapid += 1
        if currentmapid > maxmapid:
            maxmapid += 1
        currentmap = maps[currentmapid]['data']
        cords = maps[currentmapid]['cords']['start']
        win = maps[currentmapid]['cords']['end']
    elif out[0] == False:
        cords = out[1]
        clear()
        settings = menu(currentmapid, settings, {
            "maxmapid": maxmapid,
            "modded": __modded__
        })

json.dump({
    "maxmaps": maxmapid,
    "settings": settings,
    "moddedgame": __modded__
}, open('data/save.dat', 'w'))

clear()

print("Thanks for playing! \n - MrShoe")

print("Hope you didn't find any bugs!")
print("Have a nice day!")

value = getpass.getpass("\n(Hit enter to exit) \n\n")