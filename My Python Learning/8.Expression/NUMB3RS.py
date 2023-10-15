from re import search


def main():
    print(validate(input("IPv4 address: ")))


def validate(ip):
    regec = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"
    match = search(r"^" + regec + "\." + regec + "\." + regec + "\." + regec + "$", ip)
    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    main()