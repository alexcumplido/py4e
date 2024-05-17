"""
Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.
"""

ct_day = dict()
ct_adress = dict()
femail = open("../files/mbox.txt")
for ln in femail:
    ln = ln.strip()
    ln = ln.split()
    if len(ln) == 0 or ln[0] != 'From': continue 
    ct_adress[ln[1]] = ct_adress.get(ln[1], 0) + 1
    ct_day[ln[2]] = ct_day.get(ln[2], 0) + 1
print(ct_day, ct_adress)
femail.close()

lg = None
lgemail = ""
for val in ct_adress:
    if lg is None or ct_adress[val] > lg: 
        lg = ct_adress[val]
        lgemail = f"{val} {lg}"
print(lgemail)