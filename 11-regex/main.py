import re

# Regular expressions
# Character matching in regular expressions
# Extracting data using regular expressions
# Combining searching and extracting

file_path = f"../files/"
hand = open(f"{file_path}mbox-short.txt")
for ln in hand:
    ln = ln.rstrip()
    # if re.search('^From:', ln): print(ln)
    # if re.search('^F..m:.+@', ln): print(ln)
    # ln = re.findall('\S+@\S+', ln)
    # ln = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', ln)
    # if re.search('^X\S*:\s[0-9.]+', ln): print(ln)
    # ln = re.findall('^X\S*:\s([0-9.]+)', ln)
    # ln = re.findall('^Details:.*rev=([0-9]+)', ln)
    ln = re.findall('^From\s.*\s([0-9][0-9]):',ln)
    if len(ln) > 0: print(ln)
hand.close() 

"""
Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
"""


inp_regex = input('Enter your regular expression: ')
f_hand = open(f"{file_path}mbox.txt")
ct = 0

for ln in f_hand:
    ln = ln.strip()
    try:
        ln = re.findall(inp_regex,ln)
    except:
        print("Enter a valid regular expression")

    if len(ln) > 0: ct += 1

print(f"mbox.txt had {ct} lines that matched {inp_regex}")
f_hand.close()

"""
Exercise 2: Write a program to look for lines of the form:
"""
average = list()
file_hand = open(f"{file_path}mbox-short.txt")
for ln in file_hand:
    ln = ln.rstrip()
    ln = re.findall('^New\s.*:\s([0-9]+)',ln)
    if len(ln) > 0: average.append(int(ln[0]))
       
average = int(sum(average)/len(average))
print(f"Average: {average}")
file_hand.close() 