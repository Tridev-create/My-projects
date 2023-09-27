from sys import argv
import sys
import tabulate
import csv

#print(argv[1])

def main():
    Final_Data = []
    Import = []
    Final_Import = []
    try:
        if len(argv) == 2:
            dot = convert(str(argv[1]))
            if dot != 'csv':
                print(dot)
                sys.exit('Not a CSV file')

            with open(argv[1]) as files:
                lines = 0
                for line in files:
                    if line.lstrip() != '' and not line.lstrip().startswith('#'):
                        lines += 1
            if argv[1] == 'regular.csv':
                with open('regular.csv') as file_2:
                    Reader = csv.DictReader(file_2)
                    print(tabulate.tabulate(Reader, headers='keys', tablefmt="grid"))
                    for data in Reader:
                        Final_Data.append({'Regular Pizza': data['Regular Pizza'], 'Small': data['Small'],'Large': data['Large']})

                for Final_Data_2 in Final_Data:
                    Final_Import = ([Final_Data_2['Regular Pizza']], [Final_Data_2['Regular Pizza']],[Final_Data_2['Regular Pizza']])
            elif argv[1] == 'sicilian.csv':
                with open('sicilian.csv') as file_3:
                    Reader = csv.DictReader(file_3)
                    print(tabulate.tabulate(Reader, headers='keys', tablefmt="grid"))
                    for data in Reader:
                        Final_Data.append({'Sicilian Pizza': data['Regular Pizza'], 'Small': data['Small'],'Large': data['Large']})

                for Final_Data_2 in Final_Data:
                    Final_Import = ([Final_Data_2['Sicilian Pizza']], [Final_Data_2['Regular Pizza']],[Final_Data_2['Regular Pizza']])


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