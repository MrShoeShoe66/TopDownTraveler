import PyInstaller.__main__ as PyInstaller

PyInstaller.run([
    './src/main.py',
    '--console',
    '-i=./icon.ico',
    '--clean',
    '--noconfirm',
    '--name=TDT',
    '--onedir',
    '--add-data=./src/data/map.dat;./data/',
    '--add-data=./src/data/save.dat;./data/',
    '--add-data=./src/data/note.txt;./data/'
])

import shutil

shutil.rmtree("./build")
try:
    shutil.rmtree("./TDT/dist")
except:
    pass

original = './dist'
target = './TDT/dist'

shutil.move(original, target)

