#dict
fname = input("Enter filename: ")
handle = open(fname)
d={}

for line in handle:
    line = line.rstrip()
    split_line = line.split()
    for words in split_line:
        d[words] = d.get(words,0)+1
print(d)