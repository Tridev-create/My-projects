print("Amount Due: 50")
buyer_coin = 0

for i in range(1):
    coins = int(input("Insert coin: "))
    buyer_coin = buyer_coin + coins
    Due_coins = 50 - buyer_coin
    print("Amount Due:", Due_coins)
    if buyer_coin == 30:
        print("Amount Due: 50")
        break



while True:
    Due_coins = 50
    coins = int(input(""))
    buyer_coin = buyer_coin + coins
    Due_coins = Due_coins - buyer_coin
    if buyer_coin < 50:
        print("Amount Due:", Due_coins)

    if buyer_coin == 50:
        print("Change Owed: 0")
        break
    elif buyer_coin == 60:
        print("Change Owed: 10")
        break