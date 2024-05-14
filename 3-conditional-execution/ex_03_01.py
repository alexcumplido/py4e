"""
Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
"""
hrs = input("Enter Hours: ")
rate = input("Enter rate: ")
try:
  float_hours = float(hrs)
  float_rate = float(rate)
except:
  print("Error please enter a numeric input")
  quit()

if float_hours > 40: # Overtime
  regular_pay = 40 * float_rate 
  overtime_pay = (float_hours - 40) * (float_rate * 0.5)
  gross_pay = regular_pay + overtime_pay
  print(gross_pay)

else: # Regular
  gross_pay = float_hours * float_rate

print(gross_pay)
