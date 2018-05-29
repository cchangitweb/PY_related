# data type 

width = 17
height = 12.0 

print (width, type(width))         # 7 <class 'int'>
print(height, type(height))        # 12.0 <class 'float'>
print(width//2, type(width))       # 8 <class 'int'>  
print(width//2.0, type(width/2.0)) # 8.0 <class 'float'>
print(height/3, type(height/3))    # 4.0 <class 'float'>
print(1+2*5, type(1+2*5))          # 11 <class 'int'>

# convert Celsius to Fahrenheit

quotient = 7//3                    # 2
print(quotient)

qo = 7/3                           # 2.3333333333333335
print(qo)

Cel = "Enter Celsius: "
cel = input(Cel)
fah = float(cel) * 9 /5 + 32

print('Celsius is :', cel)
print('Fahrenheit is :', fah)
