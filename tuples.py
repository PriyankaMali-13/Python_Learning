a = ('A','B')
print(a)

(a,b) = ('C','D')
print(a,b)

#sorting with value
d = {'a':1,'b':32,'c':6}
l = []
for k,v in d.items():
    l.append((v,k))
print(l)
l=sorted(l)
print(l)

#quix
x,y = 3,4
print(x,y)

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)