import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(i):
    if validators.email(i) == True:
        return f"Valid"
    else:
        return f"Invalid"


if __name__ == "__main__":
    main()