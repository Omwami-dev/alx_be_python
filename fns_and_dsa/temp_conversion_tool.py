FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit (celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
temp = input("Enter the temperature to convert: ")
unit = input("Is this temperature in celsius or Fahrenheit? (C/F): ")
if unit == "c":
    converted_temp = convert_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {converted_temp:.2f}°F")
elif unit == "F":
    converted_temp = convert_to_celsius(temp)
    print(f"{temp}°F is equal to {converted_temp:.2f}°C")
else:
    print("Invalid input. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
if __name__ == "__main__":
    main()
