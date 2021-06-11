#Convert elevator floors
inp = input("European floor?")
ans = int(inp)+1
print('US floor:',ans)

#prints the div of two nos
print(42%10)

#print the value of x after solving expression
x = 1 + 2 * 3 - 8 / 4
print(x)

#converts x from float to int & prints the roundoff value of x
x = int(98.6)
print(x)

'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
You should use input to read a string and float() to convert the string to a number. 
'''
hrs = input("Enter Hours:")
rate = input("Enter rate:")
ans = float(hrs)* float(rate)
print("Pay:",ans)