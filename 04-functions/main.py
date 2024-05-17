""" Functions """
""" type conversion functions"""
int('32')
int(3.9)
int(-2.9214)
float(32)
float(3.14159)
str(32)

import random
"""
for i in range(10):
   x =  random.random()
   print(x)
"""

"""built-in functions or methods"""
x = random.randint(5,10)
print(x)

y = random.choice([1,2,3])
print(y)

"""user-defined functions"""
def print_lyric(name):
    print('Everyone gets what they want')
    print(f"What are you looking for {name} ?")

# print(print_lyric("Alexandre"))

def repeat_lyrics(name):    
    print_lyric(name)
    print_lyric(name)

# repeat_lyrics(input())

def computepay(hrs, rate):
    hrs = input("Enter Hours: ")
    rate = input("Enter rate: ")
    try:
        float_hours = float(hrs)
        float_rate = float(rate)
        if float_hours > 40: # Overtime
            overtime_pay = (float_hours - 40) * (float_rate * 0.5)
            gross_pay = 40 * float_rate + overtime_pay
        else: # Regular
            gross_pay = float_hours * float_rate
        print(gross_pay)
    except:
        print("Error please enter a numeric input")
        quit() 

# computepay(45,10)

def computegrade(score):
    try:
        score = float(input("Enter Score: "))
        if score >= 0.0 and score <= 1.0:
            if score < 0.6:
                print("F")
            elif score < 0.7:
                print("D")
            elif score < 0.8:
                print("C")
            elif score < 0.9:
                print("B")
            else:
                print("A")
        else:
            print("Insert a score between 0.0 and 1.0")
    except:
        print("Bad score, insert a valid number")

computegrade(0.95)