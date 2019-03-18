a=int(input()) #input of data
b=int(input())
c=int(input())
d=int(input())

print('\t', end=' ')
for i in range(c, d+1): # print the first line 
    print(i, '\t', end=' ')
print()

for i in range(a, b+1): 
    print(i, '\t', end='')
    for g in range(c, d+1):
        print(i*g, '\t', end='')
    print()
