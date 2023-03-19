#==> 4-1
pizzas = ['Bbq','Grilled','Fajita']

for pizza in pizzas:
    print(pizza)

print()

for pizza in pizzas:
    print("This pizza flavour is: "+pizza)

print("I like thin crust pizzas.\nI like Chicken Pizzas.\nI like Spicy Pizzas.\nI really love pizza. ")
    
print()
print()

    
#==> 4-2
animals = ['Lion','Tiger','Cheetah']
for animal in animals:
    print(animal)
    
print()
    
for animal in animals:
    print(animal + " won't be a great pet.")

print("All these animals have 4 legs")

print()    
print()

#==> 4-3
for i in range(1,21):
    print(i)
    
#==> 4-4
num_list = []
for i in range(1,pow(10,6)+1):
    num_list.append(i)
    
for num in num_list:
    print(num)
    
print()
print()
    
#==> 4-5
num_list = []
for i in range(1,pow(10,6)+1):
    num_list.append(i)
    
print("Max Number of the list is: "+ str(max(num_list)))
print("Min Number is: "+ str(min(num_list)))

print("Sum of the list items is: ")
print(sum(num_list))

print()
print()

#==> 4-6
num_list = []
for i in range(1,21,2):
    num_list.append(i) 
for num in num_list:
    print(num)

print()
print()

#==> 4-7
num_list = []
for i in range(3,31,3):
    num_list.append(i)
for num in num_list:
    print(num)

print()
print()

#==> 4-8
num_list = []

for i in range(1,11):
    num_list.append(i**3)
for num in num_list:
    print(num)
    
print()
print()
#==> 4-9
cubes = [value**3 for value in range(1,11)]
for num in cubes:
    print(num)
