FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * fahrenheit - 32
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
    return fahrenheit

fahranite = float(input("Enter fahranite: "))
convert_to_celsius(fahrenheit)
celsius = float(input("Enter celsius: "))
convert_to_fahrenheit(celsius)