import curses

# define the menu function
def rendermenu(title, description, classes, note='Hit Enter to Continue', color='white'):
  # define the curses wrapper
  def character(stdscr,):
    attributes = {}
    # stuff i copied from the internet that i'll put in the right format later
    icol = {
      1:'blue',
      2:'green',
      3:'yellow',
      4:'red',
      5:'magenta',
      6:'cyan',
      7:'white'
    }
    # put the stuff in the right format
    col = {v: k for k, v in icol.items()}

    # declare the background color

    bc = curses.COLOR_BLACK

    # make the 'normal' format
    curses.init_pair(1, 7, bc)
    attributes['normal'] = curses.color_pair(1)


    # make the 'highlighted' format
    curses.init_pair(2, col[color], bc)
    attributes['highlighted'] = curses.color_pair(2)


    # handle the menu
    c = 0
    option = 0
    while c != 10:

        stdscr.erase() # clear the screen (you can erase this if you want)

        # add the title
        stdscr.addstr(f"{title}\n\n", curses.color_pair(1))

        if description != '':
            stdscr.addstr(f"{description}\n\n", curses.color_pair(1))

        # add the options
        for i in range(len(classes)):
            # handle the colors
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            
            # actually add the options

            stdscr.addstr(f'> ', attr)
            stdscr.addstr(f'{classes[i]}' + '\n', attr)

        stdscr.addstr(f"\n", curses.color_pair(1))
        stdscr.addstr(f"{note}\n", curses.color_pair(1))

        c = stdscr.getch()

        # handle the arrow keys
        if c == ord("w") and option > 0:
            option -= 1
        elif c == ord("s") and option < len(classes) - 1:
            option += 1
    return option
  return curses.wrapper(character)

#  print("output:", rendermenu('TEST', 'desc', [0,1,2,3,4,5,6,7,8,9,10], 'Note', 'blue'))