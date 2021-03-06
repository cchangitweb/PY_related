# example of iteration 
n = 5
while n > 0:
    print(n)
    n = n-1
print('Blastoff!')

# infinite loop 1
# m = 10
# while True:
#   print(m, end=' ')
#    m = m - 1
# print('Done !')

# infinite loop 2 with break
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
type(line)

count = 0 
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

friends = ['Joe','Glenn','Sally']
for friend in friends:
    print('Happy New Year: ', friend)
print('Done!')

""" # output
5
4
3
2
1
Blastoff!
> #100
> d0ne
d0ne
> done
Done!
Count:  6
Happy New Year:  Joe
Happy New Year:  Glenn
Happy New Year:  Sally
Done!
""" # end of output 


​
