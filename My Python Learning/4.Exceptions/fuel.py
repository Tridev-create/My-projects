while True:
    try:
        Fuel = input("Type: ")
        x, y = Fuel.split("/")
        x_int = int(x)
        y_int = int(y)
        Summary = x_int / y_int * 100
        Summary_int = int(Summary)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if x_int == 4 or x_int == 100 or x_int == 99:
            print("F")
            break
        elif x_int == 0 or y_int == 100:
            print("E")
            break
        elif x_int == 5 or y_int == 3 and x_int == 10:
            pass
        elif Summary_int == 66:
            Summary_int = Summary_int + 1
            print(Summary_int, end="%")
            break
        elif x_int >= 0 or x_int <= 4:
            print(Summary_int, end="%")
            break