import PyInstaller.__main__ as PyInstaller

PyInstaller.run([
    './src/main.py',
    '--console',
    '-i=../icon.ico',
    '--clean',
    '--noconfirm',
    '--name=TDT',
    '--onedir',
    '--add-data=../src/map.dat;.',
    '--add-data=../src/save.dat;.'
])