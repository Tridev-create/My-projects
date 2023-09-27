Summary = 0

key = {
        "Baja Taco": 4.00,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }

while True:
    try:
        item = input("Item: ")
        if item in key:
            Summary += key[item]
            print(f"Total: ${Summary:.2f}")


    except EOFError:
        print()
        break
    except KeyError:
        pass