#=> 10-1
with open('learning_python.txt') as file:
    contents = file.read()
    print(contents)
print()
#loop
with open('learning_python.txt') as file:
    for line in file:
        print(line)
print()
#Making list of lines
with open('learning_python.txt') as file:
    lines = file.readlines()
for line in lines:
    print(line)
    
print()
print()

#=> 10-2
with open('learning_python.txt') as file:
    lines = file.readlines()
for line in lines:
    line.replace('Python','C')
    print(line)
print()
print()

#=> 10-3
name = input("Please Enter Your name: ")
with open('guest.txt','w') as file:
    file.write(name+'\n')

#=>10-4

while (True):
    with open('guest_book.txt','a') as file:
        name = input("Enter your name: ")
        file.write(name+' Visited\n')
        print('Welcome '+name)


