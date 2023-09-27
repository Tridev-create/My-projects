from pyfiglet import Figlet, figlet_format
from sys import argv
from sys import exit
from random import randint , choice

figlet = Figlet()

f = figlet.getFonts()

f_str = str(f)

txt = argv[1]

if len(argv) == 1:
    figlet.setFont(font=choice(f))
elif argv[2] in f and len(argv) == 3 and argv[1] == '--font' or argv[1] == '-f':
    figlet.setFont(font=argv[2])
else:
    exit('Invalid usage')

result = input('Input: ')
print(figlet.renderText(result))
