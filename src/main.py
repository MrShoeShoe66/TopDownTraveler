import keyboard, os, time, sys, json, getpass

__version__ = "Release 1"

def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear') 

sys.stdout.write("\x1b]2;Top Down Traveler\x07")

clear()

global settings

settings = {
    "color": False,
    "debug": False
}

global maps
global mapcount

mapdat = json.load( open('map.dat') )

maps = mapdat['data']
mapcount = len(maps)

global modded

modded = mapdat['modded']

__mapversion__ = mapdat['mapfileversion']

__modded__ = mapdat['modded']

global maxmapid
global currentmapid
global currentmap
global cords
global win

savedata = json.load( open('save.dat') )

maxmapid = savedata['maxmaps']
currentmapid = maxmapid

if maxmapid == mapcount:
    print("Hey! The save file your using is completed! Thanks for playing my game!")
    currentmapid = 0

currentmap = maps[currentmapid]['data']
cords = maps[currentmapid]['cords']['start']
win = maps[currentmapid]['cords']['end']
settings = savedata['settings']

def settingsmenu():
    while True:
        clear()
        settingsoption = input(f"""
--- ################################## ---
                 Settings
--- ################################## ---

 1 - Colored Menu: {settings['color']}
 2 - Back

Version - {__version__}

Select an option > """)
        if settingsoption == "1":
            settings['color'] = not settings['color']
            time.sleep(1)
        elif settingsoption == '2':
            break

def levelselectrender(selected, max, page):
    output = ''

    topbot = ''
    midpad = ''
    mid = ''

    for i1 in [1,2,3,4,5]:
        i = i1 + 5 * page
        if i <= max:

            if i == selected:
                topbot = f'{topbot}# # # # #   '
            else:
                topbot = f'{topbot}- - - - -   '

            if i == selected:
                midpad = f'{midpad}#       #   '
            else:
                midpad = f'{midpad}-       -   '

            if i > 99:
                if i == selected:
                    mid = f'{mid}#  {i}  #   '
                else:
                    mid = f'{mid}-  {i}  -   '
            elif i > 9:
                if i == selected:
                    mid = f'{mid}#   {i}  #   '
                else:
                    mid = f'{mid}-   {i}  -   '
            else:
                if i == selected:
                    mid = f'{mid}#   {i}   #   '
                else:
                    mid = f'{mid}-   {i}   -   '

    output = f'{topbot}\n{midpad}\n{mid}\n{midpad}\n{topbot}'

    return output

def computemove(map, direction, cords):
    currentx = cords[0]
    currenty = cords[1]
    
    if map[currenty][currentx] == 1:
        raise "INVAILID START POS"
    
    if direction == 'w':
        newy = currenty - 1
        newx = currentx
    
    elif direction == 's':
        newy = currenty + 1
        newx = currentx
    
    elif direction == 'a':
        newy = currenty
        newx = currentx - 1
    
    elif direction == 'd':
        newy = currenty
        newx = currentx + 1

    else:
        newy = currenty
        newx = currentx
    
    if not map[newy][newx] != 1:
        return [currentx, currenty]
    else:
        return [newx, newy]


item = [
    ' ',
    '#',
    'W',
    'P'
]

coloreditem = [
    ' ',
    "\33[31m#",
    "\33[32mW",
    "\33[34mP"
]

def render(map, player, color):
    if color:
        internalrendersprites = coloreditem
    else:
        internalrendersprites = item
    internalmap = map
    output = ''
    output2 = ''
    internalmap[player[1]][player[0]] = 3
    for row in internalmap:
        for location in row:
            output2 = f'{output2}{internalrendersprites[location]} '
        output = f'{output}{output2}\n'
        output2 = ''
    internalmap[player[1]][player[0]] = 0
    return output[:-1]

while True:
    print("""
--- ################################## ---
             Top Down Traveler
--- ################################## ---

 1 - Play Game
 2 - Settings
 3 - How to play
 4 - Quit
 5 - Game info
""")

    menuoption = input("Select an option > ")

    if menuoption == '1':
        break
    
    if menuoption == '2':
        settingsmenu()
    
    if menuoption == '3':
        clear()
        getpass.getpass("""
--- ################################## ---
                How to play
--- ################################## ---

WASD - Move player

ESC - Pause Menu

""")

    if menuoption == '5':
        clear()
        getpass.getpass(f"""
--- ################################## ---
                Game Info
--- ################################## ---

Version - {__version__}

Map File Version - {__mapversion__}

Modded - {__modded__}

Color Mode - {settings['color']}

Debug Mode - {settings['debug']}

""")
    
    if menuoption == '4':
        exit(1)
    
    clear()

def menu():
    while True:
        clear()
        option = input(f"""
Pause Menu

 1 - Exit Game
 2 - Settings
 3 - Resume Game
 4 - Change Map
 5 - Save

Version - {__version__}

Select an option > """)
        global currentmapid
        global cords
        if option == '1':
            clear()
            print('Thanks for playing!')
            time.sleep(1)
            json.dump({
                "maxmaps": maxmapid,
                "settings": settings
            }, open('save.dat', 'w'))
            exit(1)
        elif option == "2":
            settingsmenu()
        elif option == "3":
            clear()
            break
        elif option == '4':
            currmap = currentmapid
            while True:
                clear()
                print(
                    levelselectrender(
                        currmap,
                        maxmapid,
                        int(( currmap - 1 ) / 5)
                    )
                )
                print(
                    f'Page: {int(( currmap - 1 ) / 5) + 1}/{int(( maxmapid - 1 ) / 5) + 1}'
                )

                if keyboard.is_pressed('d'):
                    if currmap != maxmapid:
                        currmap += 1
                
                if keyboard.is_pressed('a'):
                    if currmap != 1:
                        currmap -= 1
                
                if keyboard.is_pressed('enter'):
                    newmapid = currmap - 1
                    break
            if currentmapid != newmapid:
                currentmapid = newmapid
                currentmap = maps[newmapid]['data']
                cords = maps[newmapid]['cords']['start']
                win = maps[newmapid]['cords']['end']
        elif option == '5':
            json.dump({
                "maxmaps": maxmapid,
                "settings": settings
            }, open('save.dat', 'w'))

clear()

while True:
    print(render(currentmap, cords, settings['color']))
    print(f"\33[39mLevel {currentmapid+1}/{mapcount}")
    
    if keyboard.is_pressed('esc'):
        clear()
        menu()
    
    if keyboard.is_pressed('w'):
        cords = computemove(currentmap, 'w', cords)

    if keyboard.is_pressed('s'):
        cords = computemove(currentmap, 's', cords)
    
    if keyboard.is_pressed('a'):
        cords = computemove(currentmap, 'a', cords)
    
    if keyboard.is_pressed('d'):
        cords = computemove(currentmap, 'd', cords)

    
    if settings['debug']:
        print(f'MAP: {currentmap}')
        print(f'MAP ID: {currentmapid}')
        print(f'CORDS: {cords}')
        print(f'CURRENT KEY: {keyboard.read_event().name}')
    
    if cords == win:
        currentmapid += 1
        if currentmapid > maxmapid:
            maxmapid += 1
        if maxmapid == mapcount:
            break
        currentmap = maps[currentmapid]['data']
        cords = maps[currentmapid]['cords']['start']
        win = maps[currentmapid]['cords']['end']

    clear()

json.dump({
    "maxmaps": maxmapid,
    "settings": settings
}, open('save.dat', 'w'))

clear()

print("Thanks for playing! \n - MrShoe")

print("Hope you didn't find any bugs!")
print("Have a nice day!")

value = getpass.getpass("\n(Hit enter to exit) \n\n")