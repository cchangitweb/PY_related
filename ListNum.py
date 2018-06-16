# enter a list of numbers and find max and min
# print sorted numbers
# created: June 16, 2018 (first version)

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
