## User input
try:
  celsius = input("Enter temperature in Celsius: ")
  fahrenheit = float(celsius) * 9/5 + 32
  print(fahrenheit)
except:
  print("Insert a valid number as celsius temperature")
