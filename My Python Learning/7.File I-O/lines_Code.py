from sys import argv
import sys

#print(argv[1])

def main():
    try:
        if len(argv) == 2:
            dot = convert(str(argv[1]))
            if dot != 'py':
                print(dot)
                sys.exit('Not a Python file')

            # if argv[1] in num:
            #     # sys.exit(num[argv[1]])
            # with open(argv[1], "a") as file:
            #     Add_Data = file.write('3')
            #     print(Add_Data)
            # with open(argv[1], 'r') as file:
            #     read_content = file.read()
            #     print(read_content)

            with open(argv[1]) as files:
                lines = 0
                for line in files:
                    if line.lstrip() != '' and not line.lstrip().startswith('#'):
                        lines += 1
                print('Heyy', lines)
               # print(lines)
        elif len(argv) < 2:
            sys.exit('Too few arguments')

        elif len(argv) > 2:
            sys.exit('Too many command-line arguments')

    except FileNotFoundError:
        sys.exit('File not found')
    except ValueError:
        sys.exit('Not a Python file')

def convert(argv):
    argv = str(argv)
    _, dot = argv.split('.')
    return dot

main()