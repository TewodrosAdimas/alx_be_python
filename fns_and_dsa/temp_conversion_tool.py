FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    print(f"{fahrenheit}°F is {celsius:.2f}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR + 32) * celsius
    print(f"{celsius}°C is {fahrenheit:.2f}°F")

temp = float(input("Enter the temperature to convert: "))
choose = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if choose == "f":
    convert_to_celsius(temp)
elif choose == "c":
    convert_to_fahrenheit(temp)
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
