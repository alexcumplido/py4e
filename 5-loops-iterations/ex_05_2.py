"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.
"""
lg = None
sm = None
nums = list()

while True:
    num = input("Enter a number: ")
    if num == "done": break 
    try:
        nums.append(int(num))
    except:
        print("Invalid input")
        continue
    for value in nums:
        if lg is None or value > lg: lg = value
    for value in nums:
        if sm is None: sm = value
        elif value < sm: sm = value

print(f"Maximum is {lg}")
print(f"Minimum is {sm}")