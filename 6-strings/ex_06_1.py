"""
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.

Find the substring including the number 
Slice it from the original string
Convert the string into a floating point number
Print out

"""
text = "X-DSPAM-Confidence:    0.8475"
str_sliced= text[text.find("0"):]
to_float = float(str_sliced)
print(to_float, type(to_float))