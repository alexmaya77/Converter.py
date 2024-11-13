temperature_fahrenheit = 100
print ( f"temperature in fahrenheit: {100} °F")
temperature_celsius = (temperature_fahrenheit - 32) * (5 / 9)
print( f"temperature in Celsius: {temperature_celsius:.2f} °C")
user_input = float(input("100: "))
temperature_celsius_input = (user_input - 32) * (5 / 9)
print(f"Temperature in Celsius from user input: {temperature_celsius_input:.2f} °C")