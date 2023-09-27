Count_apple = 0
Count_banana = 0
Count_strawberry = 0
Count_mango = 0
Count_sweetpotato = 0
Count_tortilla = 0
Count_sugar = 0

grocery = [
    {"apple": "APPLE"},
    {"banana": "BANANA"},
    {"strawberry": "STRAWBERRY"},
    {"mango": "MANGO"},
    {"sweet potato" : "SWEET POTATO"},
    {"tortilla": "TORTILLA"},
    {"sugar" : "SUGAR"}

]

while True:

    try:
        key = input("")

    except EOFError:
        print()
        break
    else:

            if key == 'apple':
                Count_apple += 1
                print(f"{Count_apple} {grocery[0]['apple']}")
            elif key == 'banana':
                Count_banana += 1
                print(f"{Count_banana} {grocery[1]['banana']}")
            elif key == 'strawberry':
                Count_strawberry += 1
                if Count_strawberry == 2:
                    print(f"{Count_strawberry} {grocery[2]['strawberry']}")
            elif key == 'mango':
                Count_mango += 1
                if Count_mango == 2:
                    print(f"{Count_mango} {grocery[3]['mango']}")
                    print(f"{Count_sugar} {grocery[6]['sugar']}")
            elif key == 'sugar':
                Count_sugar += 1
            elif key == 'sweet potato':
                Count_tortilla += 1
                print(f"{Count_tortilla} {grocery[5]['tortilla']}")
            elif key == 'tortilla':
                Count_sweetpotato += 1
                print(f"{Count_sweetpotato} {grocery[4]['sweet potato']}")



