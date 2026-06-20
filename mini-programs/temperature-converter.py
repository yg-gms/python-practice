def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():

    choice = input("Choose conversion method (1 or 2): ").strip()
    temp = float(input("Temperature: ").strip())

    if choice == "1":
        converted_temp = celsius_to_fahrenheit(temp)
        print(f"{temp} °C = {round(converted_temp, 1)} °F")

    elif choice == "2":
        converted_temp = fahrenheit_to_celsius(temp)
        print(f"{temp} °F = {round(converted_temp, 1)} °C")

    else:
        print("Wrong choice!")

main()