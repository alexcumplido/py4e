"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
files_path = f"../files/"
ct_hours = dict()
femail = open(f"{files_path}mbox-short.txt")
for ln in femail:
    ln = ln.strip().split()
    if len(ln) == 0 or ln[0] != 'From': continue
    time = ln[5].split(":")[0]
    ct_hours [time] = ct_hours.get(time, 0) + 1

hr_lst = list()

for k, v in ct_hours.items(): hr_lst.append((k, v))

hr_lst = sorted(hr_lst)

for v, k in hr_lst: 
    print(f"{v} {k}")