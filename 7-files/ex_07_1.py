"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475s
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

"""
file_path = f"../files/"
# Use the file name mbox-short.txt as the file name
input_ex = input('Enter the file name: ')
try:
    fhand_ex = open(f"{file_path}{input_ex}", 'r')
except:
    print(f'File {input_ex} cannot be opened')
    quit()

spancount = 0
strcondition = "X-DSPAM-Confidence:"
spantotal = 0
for line in fhand_ex:
    if not line.startswith(f"{strcondition}"):
        continue
    sliced_line = line.find(' ')
    to_float = float(line[sliced_line:])
    spancount = spancount + 1
    spantotal = spantotal + to_float

print(f"Average spam confidence: {spantotal / spancount}")
fhand_ex.close()