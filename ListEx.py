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

print(' = = = =  list c  = = = ')
a = ['a', 'b', 'c']
b = ['1', '2', '3']
c = a * 5 + 2 * b
# d = a * b * a /* TypeError -> no: list * list, yes: list * numbers, yes:  list + list 

print (c)

print(' ===== output: c[0:4] ===== ')
print (c[0:4])

print(' ===== output: c[14:] ===== ')
print (c[14:])

c[3:9]= ['q', '9', 'y', '6', 'p', '8']
print(" ===== output: c[3:9]= ['q', '9', 'y', '6', 'p', '8'] ===== ")
print(c)

# output - 
# = = = =  list c  = = = 
# ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', '1', '2', '3', '1', '2', '3']
# ===== output: c[0:4] ===== 
# ['a', 'b', 'c', 'a']
# ===== output: c[14:] ===== 
# ['c', '1', '2', '3', '1', '2', '3']
# ===== output: c[3:9]= ['q', '9', 'y', '6', 'p', '8'] ===== 
# ['a', 'b', 'c', 'q', '9', 'y', '6', 'p', '8', 'a', 'b', 'c', 'a', 'b', 'c', '1', '2', '3', '1', '2', '3']

# metheds 
