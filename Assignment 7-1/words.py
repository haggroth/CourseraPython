# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
text = fh.readlines()
for i in text:
    print i.upper().strip()