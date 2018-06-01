import random

print ('random.random 1-10:')
for i in range(10):
    x = random.random()
    print(x)
    
print(' = = = = = ')    
print('random.randint 0-99 :', random.randint(0, 99))
print(' = = = = = ')    
print('random.randrange 0-100 step 10: ', random.randrange(0, 100, 10))
print(' = = = = = ')    
t = [1,2,3]
print( 'random.choice 1-3: ', random.choice(t))
print(' = = = = = ') 
print ('random.choice abcdefg&#%^*f :', random.choice('abcdefg&#%^*f'))
print(' = = = = = ') 
print('random.uniform 1-10: ', random.uniform(1, 10))
print(' = = = = = ') 
print('random.sample abcdefg&#%^*f 4 samples : ', random.sample('abcdefg&#%^*f',4))
