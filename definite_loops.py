#for loop simple example 1
for i in [1,2,3,4,5]:
    print(i)
print('Done')

#example 2
friends = ['joe','manau','priyanka','hema']
for friend in friends:
    print(friend)
print('all friends are listed')

#counting len of a occur in string c
c = "abshjsaaadaaa"
count = 0
for i in range(len(c)):
    if c[i]=='a':
        count+=1
print(count)

#quix example
zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)