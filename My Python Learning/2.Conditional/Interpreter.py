def main():
    Information = input("Type your information: ")

    First, Operator, Last = Information.split(" ")

    First_float = float(First)
    Last_float = float(Last)

    Summary = Calculate(First_float, Operator, Last_float)

    print(f"{Summary:.1f}")

def Calculate(F, O, L):
    if O == '+':
       return F + L
    elif O == '-':
        return F - L
    elif O == '*':
        return F * L
    elif O == '/':
        return F / L
    else:
        print("Not Found")


main()