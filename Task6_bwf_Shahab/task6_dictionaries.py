#=> 6-1
person = {
    'first_name':'Ahmed',
    'last_name':'Munir',
    'age': 21,
    'city':'Rawalpindi'
}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

print()
print()
#=> 6-2
fav_numbers = {
    'Ahmed':1,
    'Abdullah':2,
    'Ali':3,
    'Saad':4,
    'Khan':5,
}
print("Ahmed's favorite number is: "+str(fav_numbers['Ahmed']))
print("Abdullah's favorite number is: "+str(fav_numbers['Abdullah']))
print("Ali's favorite number is: "+str(fav_numbers['Ali']))
print("Saad's favorite number is: "+str(fav_numbers['Saad']))
print("Khan's favorite number is: "+str(fav_numbers['Khan']))

print()
print()

#=> 6-3
glossary = {
    'Conditionals':'If and while test cases',
    'dataTypes':'types of data or variables in python',
    'toUpperCase':'function that turns string to upper case',
    'remove':'function that removes item from list',
    'append':'function that adds items to the list',
}
print('Conditionals: '+glossary['Conditionals'])
print('Datatypes: '+glossary['dataTypes'])
print('ToUpperCase(): '+glossary['toUpperCase'])
print('remove(): '+glossary['remove'])
print('append(): '+glossary['append'])

print()
print()

#=> 6-4
glossary = {
    'Conditionals':'If and while test cases',
    'dataTypes':'types of data or variables in python',
    'toUpperCase':'function that turns string to upper case',
    'remove':'function that removes item from list',
    'append':'function that adds items to the list',
    'tolowerCase':'function tha turns string to lower case',
    'title':'Function turns string to title format, first letter upper case',
    'list':'A collection of items',
    'print':'Used to print things',
    'len':'function that returns length of the list'
}

for name, meaning in glossary.items():
    print(name+": "+meaning)
    
print()
print()

#=> 6-5
rivers = {
    'Nile':'Egypt',
    'Indus':'Pakistan',
    'Ravi':'Pakistan'
}
for river,country in rivers.items():
    print(river+" runs through "+country)
for river,country in rivers.items():
    print(river)
for river,country in rivers.items():
    print(country)
    
print()
print()

#=> 6-6
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 'Ali':'',
 'Khan':''
 }
for name,langauge in favorite_languages.items():
    if(langauge!=''):
        print('Thank You '+name+' for responding.')
    else:
        print(name+' Kindly take the pole')    
print()
print()


#=> 6-7
person1 = {
    'first_name':'Ahmed',
    'last_name':'Munir',
}
person2 = {
    'first_name':'Shahab',
    'last_name':'Ali',
}
person3 = {
    'first_name':'Saad',
    'last_name':'Khan',
    
}

people = [person1,person2,person3]

for human in people:
    print('First Name: '+human['first_name']+' --- '+'Last Name: '+human['last_name'])

print()
print()
    
#=> 6-8
cat = {
    'name':'Bob',
    'owner':'John',
}
dog = {
    'name':'Tommy',
    'owner':'Ahmed',
}

lion = {
    'name':'Simba',
    'owner':'Ali'
}

pets = [cat,dog,lion]

for pet in pets:
    print('Name: '+pet['name'])
    print('Owner: '+pet['owner'])
    print()
    
    
#=> 6-10
fav_numbers = {
    'Ahmed':[1,12],
    'Abdullah':[8,10],
    'Ali':[0,99],
    'Saad':[7,10]
}

for name,numbers in fav_numbers.items():
    print('Favourite Numbers of '+name+ ' are: ')
    for number in numbers:
        print(number)

#=> 6-11

cities = {
    'Rawalpindi':{
        'country':'Pakistan',
        'population':'10 Million',
        'fact':'Military City'
    },
    'Islamabad':{
        'country':'Pakistan',
        'population':'6 Million',
        'fact':'Capital of Pakistan'
    },
    'Lahore':{
        'country':'Pakistan',
        'population':'20 Million',
        'fact':'Capital of Punjab'
    }
}

for city,city_info in cities.items():
    print("\n City Name: "+ city)
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    
    print("\tCountry: "+country)
    print("\tPopulation: "+population)
    print("\tfact: "+fact)

print()
print()    

#------
info = {
    'color':'gray'
}
print(info)
# Adding to a dictionary
info['size'] = "Large"
print(info)

# Removing From a dictionary
del info['color']
print(info)

# Modifying a Dictionary
info['size'] = 'small'
print(info)
