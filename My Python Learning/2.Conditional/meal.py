def main():
    Time = input("What time is it?? : ")
    Hours_float = convert(Time)

    if Hours_float >= 6 and Hours_float <= 10:
        print("breakfast time")
    elif Hours_float >= 12 and Hours_float <= 17:
        print("lunch time")
    elif Hours_float >= 18:
        print("dinner time")


def convert(time):

    Hours, Minutes = time.split(":")
    Demical_hours = float(Hours) + (float(Minutes) / 60)
    return (Demical_hours)



if __name__ == "__main__":
    main()