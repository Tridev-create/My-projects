def main():
    Dollars = input("Enter your dollars: ")
    Dollars_str = Dollars.replace("$", "")
    Dollars = float(Dollars_str)
    Percentage = input("Enter your percentage of tips: ")
    percentage_str = Percentage.replace("%", "")
    percentage = float(percentage_str)
    Tips = dollars(Dollars) * percent(percentage) / 100
    print(f"Leave ${Tips:.2f}")

def dollars(n):
    return float(n)

def percent(n):
    return float(n)

main()