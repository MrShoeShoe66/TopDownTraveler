import curses
import render, tools, colorren

# define the menu function
def playmap(map, metadata):
  def character(stdscr,):
    attributes = {}
    icol = {
      1:'blue',
      2:'green',
      3:'yellow',
      4:'red',
      5:'magenta',
      6:'cyan',
      7:'white'
    }
    col = {v: k for k, v in icol.items()}
    bc = curses.COLOR_BLACK
    curses.init_pair(1, 7, bc)
    attributes['normal'] = curses.color_pair(1)
    attributes['highlighted'] = curses.color_pair(2)

    startingcords = metadata['playercords']
    endingcords   = metadata['wincords']
    colorsetting  = metadata['color']
    mapid         = metadata['mapid']
    maps          = metadata['mapcount']

    # handle the menu
    c = 0
    cords = metadata['playercords']
    fininshed = False
    while c == c:

        mapren = render.render(map, cords, metadata['color'])

        stdscr.erase()
        # for i in range(len(classes)): # render menu
        #     # handle the colors
        #     if i == option:
        #         attr = attributes['highlighted']
        #     else:
        #         attr = attributes['normal']
            
        #     # actually add the options

        #     stdscr.addstr(f'> ', attr)
        #     stdscr.addstr(f'{classes[i]}' + '\n', attr)

        if metadata['color']:
                colorren.PrintAsColor(stdscr, mapren)
        else:
                stdscr.addstr(mapren)

        stdscr.addstr(f"\n", curses.color_pair(1))

        currentmapid = metadata['mapid']
        mapcount = metadata['mapcount']

        stdscr.addstr(f"Level {currentmapid+1}/{mapcount}\n")

        if metadata['debug']:
                stdscr.addstr(f"\n-=-=- DEBUG MENU -=-=-\nCords {cords}\nStarting Cords {startingcords}\nEnding Cords {endingcords}\nColor Setting {colorsetting}\nMap ID {mapid}\nMap Count {maps}\nDebug True\n-=-=- DEBUG MENU -=-=-")

        c = stdscr.getch()

        if c == ord("w"):
                cords = tools.computemove(map,"w",cords)
        elif c == ord("a"):
                cords = tools.computemove(map,"a",cords)
        elif c == ord("s"):
                cords = tools.computemove(map,"s",cords)
        elif c == ord("d"):
                cords = tools.computemove(map,"d",cords)
        
        elif c == 27:
                fininshed = False
                break   

        if cords == metadata['wincords']:
                fininshed = True
                break
    return [fininshed, cords]
  return curses.wrapper(character)

# out = playmap([
#    [1,1,1,1,1],
#    [1,0,0,0,1],
#    [1,0,0,0,1],
#    [1,0,0,2,1],
#    [1,1,1,1,1]
# ], {
#    "playercords": [1,1],
#    'wincords': [3,3],
#    "color": False
# })
# print(out)