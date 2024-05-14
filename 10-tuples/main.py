import string

"""
Tuples are immutable
"""

t = tuple('lupins')
try:
    t[0] = 'L'
except:
    t = tuple('L') + t[1:]
    print(t)

"""
Comparing tuples
"""

if (1,0,0) > (0,1,1): print("First bigger")

""" 
DSU pattern
Decorate
Sort
Undecorate
"""

txt = 'but soft what light in yonder window break'
words = txt.split()
t = list()
for word in words: 
    t.append((len(word), word))
t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)
print(res)
# print(res)

"""
Tuples assignment
"""

addr = 'monty@python.org'
uname, domain = addr.split('@')
print(f"uname: {uname}, domain: {domain}")

"""
Dictionaries and tuples
"""

d = {'b':1, 'a':10, 'c':22}
t = list(d.items())
t.sort()
# print(t)

"""
Multiple assignment with dictionaries
"""

dic = {'a':10, 'b':1, 'c':22}
l = list()
for key, val in dic.items(): 
    l.append((val, key))
l.sort(reverse=True)
print(l)


dic = {'a':100, 'b':1, 'c':2222}
new_dic = sorted( [ (v, k ) for k,v in dic.items()] )

"""
The most common words
"""

fhand = open('../files/romeo-full.txt')
counts = dict()
for ln in fhand:
    ln = ln.rstrip()
    ln = ln.translate(ln.maketrans("", "", string.punctuation))
    ln = ln.lower()
    ln = ln.split()
    for word in ln: 
        counts[word] = counts.get(word, 0) + 1
        # if word not in counts:
        #     counts[word] = 1
        # else:
        #     counts[word] += 1

lst = list()
for key, value in list(counts.items()):
    lst.append((value, key))

lst = sorted(lst, reverse=True)

for val, key in lst[:40]:
    print(f"word: {key} - {val}")

"""
Using tuples as keys in dictionaries
"""
directory = dict()
directory['Bou','Cumplido'] = 123456789
for last, first in directory:
     print(first, last, directory[last,first])

"""
List comprehension
"""

list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = []
for x in list_of_ints_in_strings:
    list_of_ints.append(int(x))

print(sum(list_of_ints))

lst_ints = [int(x) for x in list_of_ints_in_strings]
print(sum(lst_ints))

"""
Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
"""

"""
Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
"""

ct_adress = dict()
ct_hours = dict()
femail = open("../files/mbox.txt")
for ln in femail:
    ln = ln.strip().split()
    if len(ln) == 0 or ln[0] != 'From': continue
    time = ln[5].split(":")[0]
    ct_hours [time] = ct_hours.get(time, 0) + 1
    ct_adress[ln[1]] = ct_adress.get(ln[1], 0) + 1

em_lst = list()
hr_lst = list()

for k, v in ct_adress.items(): em_lst.append((v, k))
for k, v in ct_hours.items(): hr_lst.append((k, v))

em_lst = sorted(em_lst, reverse=True)
hr_lst = sorted(hr_lst)

for v, k in em_lst: print(f"@: {k} - {v}")
for v, k in hr_lst: print(f"hour: {v} - {k}")


"""
Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.

Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
"""

alph = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
alph_map = dict()
fhandler = open("../files/mbox.txt")
for ln in fhandler:
    ln = ln.strip().lower()
    if len(ln) == 0: continue
    for char in ln:
        if char in alph: alph_map[char] = alph_map.get(char, 0) + 1

alph_lst = list()

for k, v in alph_map.items(): 
    alph_lst.append((v, k))

alph_lst = sorted(alph_lst, reverse=True)

for value, key in alph_lst: 
    print(f"letter: {key} - {value}")