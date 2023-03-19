#Program 1
cubes = [value**3 for value in range(1,11)]
for num in cubes:
    print(num)
#Program 2
num_list = []
for i in range(1,11):
    num_list.append(i**3)
for num in num_list:
    print(num)
#Program 3
num_list = []
for i in range(3,31,3):
    num_list.append(i)
for num in num_list:
    print(num)
