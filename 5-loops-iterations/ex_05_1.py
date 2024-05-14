"""
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.
"""
largest = None
smallest = None
nums = list()

while True:
    num = input("Enter a number: ")
    if num == "done": break 
    nums.append(float(num))
    for value in nums:
      if largest is None or value > largest:
        largest = value
    for value in nums:
      if smallest is None:
        smallest = value
      elif value < smallest:
        smallest = value

print(f"Maximum is {largest}")
print(f"Minimum is {smallest}")