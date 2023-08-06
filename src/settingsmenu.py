import time, json
from tools import *
from version import *
from menurender import *

# global settings

def settingsmenu(settings):
    while True:
        clear()
#         settingsoption = input(f"""
# --- ################################## ---
#                  Settings
# --- ################################## ---

#  1 - Colored Menu: {settings['color']}
#  2 - Back

# version - {version}

# Select an option > """)
        if settings['debug']:
            items = [
                f"Colored Menu - {settings['color']}",
                'Back',
                "Reload settings",
                "Debug Mode - TRUE"
            ]
        else:
            items = [
                f"Colored Menu - {settings['color']}",
                'Back',
                "Reload settings"
            ]
        settingsoption = str(rendermenu('--- ################################## ---\n                 Settings\n--- ################################## ---', '', items, color='blue') + 1)
        if settingsoption == "1":
            settings['color'] = not settings['color']
            time.sleep(1)
        elif settingsoption == '2':
            break
        elif settingsoption == '3':
            settings = json.load( open('data/save.dat') )['settings']
        elif settingsoption == '4':
            settings['debug'] = not settings['debug']
    return settings