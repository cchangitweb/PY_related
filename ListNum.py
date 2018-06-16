# enter a list of numbers and find max and min
# print sorted numbers
# created: June 16, 2018 (first version)
# detail: sec 1 is done on June 16, sec 2 & 3 done before June 16
# only for exercise

# sec 1: min/ max/ sport w/ numbers list 
numbers = list()

while(True):
    n = input("Enter a number: (q: quit) ")
    
    if n == 'q':
        print(' = = = = = = = =')
        break
    
    else: 
        numbers.append(int(n))
        
if len(numbers) != 0:
    print('Max: ', max(numbers))
    print('Min: ', min(numbers))
    # for i in numbers: print(i)
    numbers.sort()
    print('Sort: ', numbers)
        
else:
    print('empty number list')
    
type(numbers)

# sec 2: not using list for avg  calculation
total = 0
count = 0

while(True): # infinite loop until done 
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
    
average = total / count 
print('Average: ', average)

# sec 3: using list for avg calculation
numlist = list()
while(True):
    inp = input('Enter a number:')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average: ', average)
