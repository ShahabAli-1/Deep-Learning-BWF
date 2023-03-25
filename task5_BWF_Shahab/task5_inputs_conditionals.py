#=> 5-2
line1 = 'xyz'
line2 = 'abc'

if(line1==line2):
    print('Equality Is True')
elif(line1!=line2):
    print('Equality not True')

if(line1.lower()==line2.lower()):
    print('Test Using lower')

num1 = 3
num2 = 4
if(num1==num2):
    print('Equal Numbers')
if(num1>num2):
    print('Num1 > Num2')
if(num1<num2):
    print('Num1 < Num2')
if(num1>=num2):
    print('Num1 >= Num2')

number = [1,2,3,4,5,6]
if 1 in number:
    print('Present.')
if 7 not in number:
    print('Not in List.')
    
    
#=> 5-4
alien_color = 'red'
if(alien_color=='green'):
    print('5 Points Earned.')
else:
    print('10 Points Earned.')

alien_color = 'red'
if(alien_color=='green'):
    print('5 Points Earned.')
else:
    print('10 Points Earned.')

    

#=> 7-1
cartype = input('What kind of rental car you like? ')
print('Customer likes '+cartype+' rental car.')

#=> 7-4
active = True
while active:
    topping = input('Enter Your Pizza Topping: ')
    if(topping== 'quit'):
        active = False
    else:
        print('Adding '+topping+' topping to the pizza')
        
        
#=> 7-6
active = True
while active:
    topping = input('Enter Your Pizza Topping: ')
    if(topping== 'quit'):
        active = False
    else:
        print('Adding '+topping+' topping to the pizza')
        
active = 1
while(active<5):
    print('1')
    active += 1
    

while(True):
    topping = input('Enter Your Pizza Topping: ')
    if(topping== 'quit'):
        break
    else:
        print('Adding '+topping+' topping to the pizza')


#-> 7-7
while(True):
    print(input('Enter Your Name: '))