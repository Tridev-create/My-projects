import re


def main():
    print(parse(input("What address of your HTML: ")))


def parse(s):
    if Link := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", s):
        return f"https://youtu.be/{Link.group(2)}"
    else:
        return None


if __name__ == "__main__":
    main()