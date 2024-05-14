"""Getting length"""

name = 'Alexandre'
name_length = len(name)
print(f"Name is {name} and it's lenght is {name_length}")

"""Traversing through a string"""

string = str(input("Enter a string: "))
index = 0
while index < len(string):
    letter = string[index]
    print(f"""Letter at index {index} is letter {letter}. Word lenght is {len(string)}""")
    index = index + 1

"""
Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
"""

input_str = str(input("Enter a string: "))
index_str = len(input_str) - 1
while index_str >= 0:
    letter = input_str[index_str]
    print(f"""Letter at index {index_str} is letter {letter}. Word lenght is {len(input_str)}""")
    index_str = index_str - 1 
   
"""Strings slices"""

str_to_slice = str(input("Enter a string: "))
init_idx = int(input("Enter the initial slice index: "))
last_idx = int(input("Enter the last slice index: "))
print(f"Slice from index {init_idx} to index {last_idx} is {str_to_slice[init_idx:last_idx]}")

""""
Exercise 2: Given that fruit is a string, what does fruit[:] mean?
"""
print("fruit"[:])

"""Loop and counting"""

string_input = input("Enter a string")
str_idx = 0
while str_idx < len(string_input):
    print(f"Index {str_idx} equals position letter {string_input[index]}")
    str_idx = str_idx + 1

count = 0
for letter in "banana":
    if letter == "a":
        count = count + 1
print(count)    

""""Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments."""

def counter(str, char):
    count_let = 0
    for lett in str:
        if lett == char:
            count_let = count_let + 1
    return count

counter("banana", "a")

"""String methods"""

dir("string")
line = 'Have a nice day'
check_start = line.startswith('h')
check_start_mapit = line.lower().startswith('h')


str_to_replace = str(input("Enter a string: "))
char_to_replace = int(input("Enter the initial slice index: "))
char_replacement = int(input("Enter the last slice index: "))
print(f"Slice from index {init_idx} to index {last_idx} is {str_to_slice[init_idx:last_idx]}")

""""
Exercise 4: There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method at:
"""

def counter_method(string_param, char_param):
    return str(string_param).count(str(char_param))

"""Parsing strings"""
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
aptos = data.find('@')
sppos = data.find(' ', aptos)
host = data[aptos+1:sppos]

"""Formated String"""