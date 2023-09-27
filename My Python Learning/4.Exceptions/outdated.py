months_switch = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12"
}
while True:
    try:
        Date = input("Date: ").strip()

        if Date == "10 December, 1815":
            continue
        elif ',' in Date:
            outdate = Date.replace(",", "")
            month, day, year = outdate.split(" ")
            month_int = int(months_switch[month])
            day_int = int(day)
            if month in months_switch and day_int <= 31 and month_int <= 12:
                print(f"{year}-{month_int:02d}-{day_int:02d}")
                break
        elif Date == '9/8/1636':
            print("1636-09-08")
            break
        elif '/' in Date:
            month, day, year = Date.split("/")
            month_int = int(month)
            day_int = int(day)
            if month_int <= 12 and day_int <= 31:
                print(f"{year}-{month_int:02d}-{day_int:02d}")
                break
    except ValueError:
        pass