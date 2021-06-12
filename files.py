#open file print lines of files and count no of files
""" file = open('test_files.txt','r')
count = 0
for i in file:
    print(i)
    count +=1
print(count) """

#open file with read mode and print each char of file(op will Writing pr)
""" file = open('test_files.txt','r')
o = file.read(10)
print(o)
 """

#using rstrip()
""" file = open('test_files.txt','r')
for line in file:
    line = line.rstrip()
    print(line) """

#write to file(replaces the existing data from the file with new data)
#if file does not exists it will create new file with the data specified in ur code
""" file = open('files.txt','w')
file.write("Hello from priyanka")
file.close() """

#append()
#add new data to existing file 
#note- it does not replace the existing file
""" file = open('files.txt','a')
file.write("\nWorking with this file")
file.close() """


    

