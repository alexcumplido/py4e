import re
files_path = f"../files/"

count = 0
numbers = list()
fhand = open(f"{files_path}regex_sum_2012384.txt")
for ln in fhand:
    ln = ln.strip()
    ln = re.findall('[0-9]+', ln)
    if len(ln) > 0:
        for num in ln: numbers.append(int(num))

for num in numbers: count += num
print(f"Sum: {count}")

