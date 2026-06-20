def main():

    time_str = input("What time is it? ").strip()

    time = convert(time_str)

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")

    elif time >= 12.0 and time <= 13.0:
        print("lunch time")

    elif time >= 18.0 and time <= 19.0:
        print("dinner time")

def convert(time):

    hours, minutes = time.split(":")

    return float(hours) + float(minutes) / 60.0


if __name__ == "__main__":
    main()