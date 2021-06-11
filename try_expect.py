#first 
name = "Priyanka"
try:
    convert_name = int(name)
except:
    convert_name = -1
print(convert_name)

#second 
x = '123'
try: 
    convert_x = int(x)
except:
    convert_x = -1
print(convert_x)

#third
name = 'Bob'
try:
    print('Hello',name) #will run
    c_n = int(name) #will not run and directly jump to expect stmt
    print('third stmt') #will never run
except:
    c_n = -1
print("All done",c_n)

#fourth
num = input("Enter no:")
try:
    ival = int(num)
except:
    ival = -1
if ival>0:
    print('Good work')
else:
    print("Bad input")