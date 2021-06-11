#if stmt 
x = 5
if x>4:
    print("Greater")
if x==5:
    print("Equal")
if x<5:
    print("Smaller")

#greatest among 3 nos(if-else)
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
if a>b and a>c :
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
else:
    print("They are Equal")

#Quiz code
if  x == 5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')