"""
Opening files
"""
file_path = f"../files/"
fhand_long = open(f"{file_path}mbox.txt", 'r','r')
print(fhand_long)
fhand_long.close()

"""Text files and lines"""
print(f"This line goes first \n and this goes on a new line.")

"""
Reading files
"""

fname = input('Enter the file name: ')
try: 
    fhand =open(f"{file_path}{fname}", 'r')
except:
    print(f'File {fname} cannot be opened')
    quit()
# count = 0
# for line in fhand:
#     count = count + 1
# print(f"Line Count {count}")

# inp = fhand.read()
# print(len(inp), inp[:20])
# print(type(inp))
# print(inp)

"""
Searching through a file
"""

for line in fhand:
    line = line.rstrip()
    # if not line.startswith(f"From:"): continue
    if line.find('@uct.ac.za') == -1: continue
    print(line)

counter = 0
for line in fhand:
    if line.startswith('Subject:'): counter = counter + 1

print('There were', counter, 'subject lines in', fname)
fhand.close()
"""
Writing files 
"""

fout = open('../files/output.txt', 'w')
line1 = input("Enter file content: ")
fout.write(f"{line1}\n")
fout.write(f"{line1}\n")
