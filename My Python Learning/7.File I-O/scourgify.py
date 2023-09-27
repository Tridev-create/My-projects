from sys import argv
import sys
import tabulate
import csv

#print(argv[1])

def main():
    File = []
    try:
        if len(argv) == 3:
            dot = convert(str(argv[1]))
            if dot != 'csv':
                print(dot)
                sys.exit('not a csv file')

            with open(argv[1]) as files:
               Reader = csv.DictReader(files)
               for i in Reader:
                    i_sep = str(i['name'])
                    first, last = i_sep.split(', ')
                    File.append({'first' : first, 'last': last, 'house': i['house']})
                    print(File)
            with open(argv[2], 'w') as file_2:
                writer = csv.DictWriter(file_2, fieldnames=['first', 'last', 'house'])
                writer.writeheader()
                for i in File:
                    writer.writerow({'first': i['last'],'last': i['first'],'house': i['house']})
                            #print(Writer)
                    # print(File)


        elif len(argv) < 3:
            sys.exit('Too few command-line arguments')

        elif len(argv) > 3:
            sys.exit('Too many command-line arguments')

    except FileNotFoundError:
        sys.exit(f'Could not read {argv[1]}')
    # except ValueError:
    #     sys.exit('Not a csv file')

def convert(argv):
    argv = str(argv)
    _, dot = argv.split('.')
    return dot

main()