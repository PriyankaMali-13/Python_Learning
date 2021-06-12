
#taking file name i/p from user
#converting char to upppercase
#Note - It doesnot convert og file char to uppercase
""" fname = input("Enter file name: ")
file = open(fname)
read_file = file.read()
strip = read_file.strip()
u=strip.upper()
print(u) """

#simple method
fname = input("Enter file name: ")
file = open(fname)
for line in file:
    line = line.rstrip()
    print(line.upper())
