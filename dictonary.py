#creating and assigning values to list
fruits = {}
fruits['apple'] = 5
fruits['banana'] = 7
fruits['grapes'] = 9
print(fruits)

#changing values of list
fruits['apple'] = 56
print(fruits)

#retriving specific value using key
print(fruits['grapes'])

#printing keys and values using in-built method
print(fruits.keys())
print(fruits.values())

#to print list of key-value pair
print(fruits.items())

#counting in dict using get to avoid trackeback
counts = {}
names = ['go','to','hell','go','once','again','to','hell','hell']
for name in names:
    counts[name] = counts.get(name,0)+1
print(counts)
    
#looping on dict using forloop and items() -> using 2 iteration variables
d = {'dogs':45,'cats':100,'lions':32}
for k,v in d.items():
    print(k,v)

#simply loops through keys in dict and print it
d = {'dogs':45,'cats':100,'lions':32}
for i in d:
    print(i)