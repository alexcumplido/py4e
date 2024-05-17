"""Lists as mutable sequences"""
list_of_strings = ["a", "b", "c"]
list_of_mixed_values = [1, ["a", "b"], 2]

print(list_of_strings, list_of_mixed_values)

list_of_strings = ["element"]
list_of_mixed_values[0] = "one"
list_of_mixed_values[1][0] = 1

print("c" in list_of_strings)
print(2 in list_of_mixed_values)
print("one" not in list_of_mixed_values)

print(list_of_strings, list_of_mixed_values)

"""Traversing lists"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for integer in nums:
    print(integer)

print(f"List of integers equals: {nums}")
for index in range(len(nums)):
    print(f"Index {index} : positioned element {nums[index]}")

"""List methods"""

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3], t[:4], t[3:])
t_cp = t[:]
t_cp[:1] = ["x", "y"]
print(t, t_cp)

t.append('g')
t.extend(['h','i','j'])
print(t)
t_cp.sort()
print(t_cp)

t_cp.remove('y') 
t_cp.pop()
del t_cp[0]
print(t_cp)


"""Lists and functions"""
print(len(nums), max(nums), min(nums), sum(nums), sum(nums)/len(nums))

"""lists and strings"""

s = 'a string of characters'
print(s.split())
print('span-span-span'.split('-'))
print(' '.join(['span','span','span']))
print(list(s))
print(s)

"""Parsing lines"""
fhand = open("../files/mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
fhand.close()

"""Objects and values"""
# Two objects can be equivalents having the same elements but not identical.
# If two objects are identical they are also equivalent.
a = 'banana'
b = 'banana'
print(a is b)
list_a = [1,2,3,4,5]
list_b = [1,2,3,4,5] 
print(list_a is list_b)

"""Aliasing lists"""
l_origin_reference = [1,2,3,4]
l_point_reference = l_origin_reference
l_point_reference[0] = 100
print(l_origin_reference)

nice_array = ["ed", "seykota"]
def del_head(param_l):
    del param_l[0]
    
filehand = open('../files/mbox-short.txt')
for line in filehand:
    string_words = line.split()
    # print('Debug:', string_words)
    if len(string_words) == 0 or string_words[0] != 'From': continue 
    print(words[2])
""""
Exercise 1: 
Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 
Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
"""

test = [1,2,3,4,5]
def chop(t):
    t[1:-1]

def middle(t):
    return  t[1:-1]
