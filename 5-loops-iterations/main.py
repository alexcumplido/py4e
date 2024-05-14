n = 5
while n > 0: #Evaluate the condition yielding True or False, if false exit the while statement and continue execution on the next one, if True execute body and then go back 1 step
    print(n) #On each iteration print the value of n
    n = n -1
print("Blastoff!")

for friend in ['Joseph', 'Glenn', 'Sallly']:
    print("Friend variable is:", friend)

count = 0
sum = 0
average = 0
print(f"Value of count: {count}, Value of sum: {sum}, Value of average: {average}")
for value in [9, 41, 12, 3, 74, 15]:
    print("Current value of sum:", sum)
    count = count + 1
    sum = sum + value

average = sum / count
print(f"Value of count: {count}, Value of sum: {sum}, Value of average: {average}")

largest = None
print(f"Initial value of largest {largest}")
for interva in [3, 41, 12, 9, 74, 15]:
    if largest is None or interva > largest:
        largest = interva
    print(largest, interva)

if largest == max([3, 41, 12, 9, 74, 15]):
    print("The largest number is:", largest)


smallest = None
print(f"Initial value of smallest {smallest}")
for value in [3, 41, 12, 9, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value

if smallest == min([3, 41, 12, 9, 74, 15]):
    print("The smallest number is:", smallest)


"""
Exercise 1: Write a program which repeatedly reads integers until the user enters “done”.
Once “done” is entered, print out the total, count, and average of the integers.
If the user enters anything other than a integers, detect their mistake using try and except and print an error message and skip to the next integers.
"""

total = 0
count = 0
average = 0

while True:
    prompt = input("Enter a number: ")
    if prompt == "done":
        break
    try:
        prompt = int(prompt)
        total = total + prompt
        count = count + 1
    except:
        print("Print a valid number")
        continue
    
average = total / count
print("Total:", total, "Count:", count, "Average:", average)

"""
Execise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
"""