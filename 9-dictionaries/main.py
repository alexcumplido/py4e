import string

""""Dictionaries"""

"""
Exercise 2: Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn’t matter what the values are. 
Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""

fhand = open('../files/words.txt', 'r')
str_dct = dict()
for line in fhand:
    lst = line.strip().split(' ')
    if '{\em' in lst: lst.remove('{\em')
    for item in lst:
        if item == '': continue
        str_dct[item] = item 
print(str_dct)  
print(list(str_dct.values()))
fhand.close() 
      
"""
Dictionary as a set of counters
"""

w = input('Enter a word: ')
w_dct = dict()
for c in w: w_dct[c] = w_dct.get(c, 0) + 1
    # if c not in w_dct:
    #     w_dct[c] = 1
    # else:
    #     w_dct[c] = w_dct[c] + 1 

# print(list(w_dct.values()))
print(w_dct)

"""
Dictionaries and files
Advanced text parsing
"""

fhand = open("../files/romeo-full.txt")
counts = dict()
for ln in fhand:
    ln = ln.rstrip()
    ln = ln.translate(ln.maketrans("", "", string.punctuation))
    ln = ln.lower()
    ln = ln.split()
    for word in ln: 
        counts[word] = counts.get(word, 0) + 1
print(counts)
fhand.close()

"""
Looping and dictionaries
"""
ct_sort = list(counts.keys())
ct_sort.sort()
for key in ct_sort: print(f"Key: {key}, value: {counts[key]}")

""""
Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.
"""