#while loop
n = 5
while n>0:
    print(n)
    n-=1
print('Done printing n')

#while loop with break stmt

while True:
    line = input(' input to test brk stmt:')
    if line=='done':
        break
    print(line)
print('break worked')

#while loop with break and continue
while True:
    line = input('input to test brk and continue stmt:')
    if line=='priyanka':
        continue
    if line=='done':
        break
    print(line)
print('break worked')
