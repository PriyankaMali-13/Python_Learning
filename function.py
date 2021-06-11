#non-parametrized function
def example():
    print('Hello Priyanka')

example() #Calling function i.e invoking the function
print("Function up nd running")



#parametrized function
def greet(lang):
    if lang=="marathi":
        print('Swaagat')
    elif lang=='en':
        print('Hello')
    else:
        print('Language not found')

greet('marathi')
greet('en')
greet('abc') #Language not found
#greet() -> TypeError: greet() missing 1 required positional argument: 'lang'



#function using return
def greetMe():
    return 'Hello'
print(greetMe(), 'Priyanka')

#multiple parameters

def add(a,b):
    ans = a+b
    return ans
print(add(13,10))

#example using max in-built function
x = 'banana'
y = max(x)
print(y)

#example of quiz
def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)