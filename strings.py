#first example
s = 'banana'
print(s)
print(type(s))

#string concatenation
a='Priyanka'
b='Mali'
ans = 'my name is'
print(ans+" "+a+" "+b)

#comparing strings
a=input("Enter first string:")
b=input("Enter second string:")
if a==b:
    print('Equal')
else:
    print('Not equal')

#string sclicing
name='priyanka mali'
res1 = name[:9]#should print priyanka
res2 = name[5:11]#should print nka ma(note:It does not ignore space)
res3 = name[-5:-2]#negative indexing (should print space ma)
print(res1) 
print(res2)
print(res3)

#looping over string
s = 'abcdefghij'
for i in range(len(s)):
    print(s[i])

#string methods
a='priyanka mali   '
print(a.lower())
print(a.upper())
print(a.capitalize())#Priyanka mali
print(a.title())#Priyanka Mali
print(a.find('li'))
print(a.replace('mali','don'))#it does not change og value
print(a.strip())