from sys import argv
import sys
import tabulate
import csv
from PIL import Image, ImageOps

#print(argv[1])

def main():
    File = []
    try:
        Our_Img = Image.open(argv[1])
        if len(argv) == 3:
            dot = convert(str(argv[1]))
            dot_2 = convert(str(argv[2]))
            print(dot_2)
            if dot != dot_2:
                print(dot)
                sys.exit('Input and output have different extensions')

            shirt = Image.open('shirt.png')
            size = shirt.size
            Our_Img = ImageOps.fit(Our_Img, size)
            Our_Img.paste(shirt, shirt)
            Our_Img.save(argv[2])



        elif len(argv) < 3:
            sys.exit('Too few command-line arguments')

        elif len(argv) > 3:
            sys.exit('Too many command-line arguments')

    except FileNotFoundError:
        sys.exit(f'Input does not exist')

def convert(argv):
    argv = str(argv)
    _, dot = argv.split('.')
    return dot

main()