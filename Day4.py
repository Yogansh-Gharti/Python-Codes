def length_converter():
    meter = float(input("Enter value in meters: "))
    print(f"Kilometers: {meter / 1000}")
    print(f"Centimeters: {meter * 100}")
    print(f"Millimeters: {meter * 1000}")


def weight_converter():
    kg = float(input("Enter value in kilograms: "))
    print(f"Grams: {kg * 1000}")
    print(f"Pounds: {kg * 2.20462}")


def temperature_converter():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15

    print(f"Fahrenheit: {fahrenheit:.2f}")
    print(f"Kelvin: {kelvin:.2f}")


while True:
    print("\n===== SMART UNIT CONVERTER =====")
    print("1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature Converter")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        length_converter()

    elif choice == "2":
        weight_converter()

    elif choice == "3":
        temperature_converter()

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
