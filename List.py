# list example
fruit = ["orange","apple","banana"]
numbers = ['1', '-34','349']
empty = ['']
print(fruit, numbers, empty)

# list size is fixed 
empty[0] = 'empty'
numbers[2] = 'bingo'
print(empty, numbers, fruit[2])

# output 
# ['orange', 'apple', 'banana'] ['1', '-34', '349'] ['']
# ['empty'] ['1', '-34', 'bingo'] banana
#

# list operations:
# 1. traverse 
# 2. + and * 

for f in fruit:
  print(f)

# output - traverse
# orange
# apple
# banana

a = ['a', 'b', 'c']
b = ['1', '2', '3']
c = a * 5 + 2 * b
# d = a * b * a /* TypeError -> no: list * list, yes: list * numbers, yes:  list + list 
print (c)

# output - 
# ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', '1', '2', '3', '1', '2', '3']

