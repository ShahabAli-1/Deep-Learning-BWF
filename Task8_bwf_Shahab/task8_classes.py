#=> 9-1
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine 
    def describe_restaurant(self):
        print('Restaurant Name: '+self.name.title()+'\nCuisine: '+self.cuisine.title())
    def open_restaurant(self):
        print('The Restaurant is Open.')
        
        
rest1 = Restaurant('XYZ','Karahi')
print(rest1.name)
print(rest1.cuisine)
rest1.describe_restaurant()
rest1.open_restaurant()


#=> 9-2
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine 
    def describe_restaurant(self):
        print('Restaurant Name: '+self.name.title()+'\nCuisine: '+self.cuisine.title())
    def open_restaurant(self):
        print('The Restaurant is Open.')

hotel1 = Restaurant('Kp','Tikka')
hotel2 = Restaurant('Rwp','Savour')
hotel3 = Restaurant('Isl','Kabab')
hotel1.describe_restaurant()
hotel2.describe_restaurant()
hotel3.describe_restaurant()


#=> 9-3
class user():
    def __init__(self,fname,lname,age,height):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.height = height
    def describe_user(self):
        print('First Name: '+self.fname)
        print('Last Name: '+self.lname)
        print('Age: '+str(self.age))
        print('Height: '+str(self.height))
    def greet_user(self):
        print('We welcome you, '+self.fname)
        
user1 = user('Shahab','Ali',20,5.10)
user2 = user('Ali','Khan',20,5.8)
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()


#=> 9-4
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine 
        self.number_served = 0
    def describe_restaurant(self):
        print('Restaurant Name: '+self.name.title()+'\nCuisine: '+self.cuisine.title())
    def open_restaurant(self):
        print('The Restaurant is Open.')
    def set_numbers_served(self,served):
        self.number_served = served
    def increment_number_served(self,served):
        self.number_served += served

restaurant = Restaurant('Savour','Rice')
print('No of customers served: '+ str(restaurant.number_served))
restaurant.set_numbers_served(10)
print('No of customers served: '+ str(restaurant.number_served))
restaurant.increment_number_served(3)
print('No of customers served: '+ str(restaurant.number_served))


#=> 9-6
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine 
        self.number_served = 0
    def describe_restaurant(self):
        print('Restaurant Name: '+self.name.title()+'\nCuisine: '+self.cuisine.title())
    def open_restaurant(self):
        print('The Restaurant is Open.')
    def set_numbers_served(self,served):
        self.number_served = served
    def increment_number_served(self,served):
        self.number_served += served

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['Vanilla','Ice','Kulfa']
    def display_flavors(self):
        print('Flavors: '+str(self.flavors))
        
iceStand = IceCreamStand('Ice Factory','Khana')
iceStand.display_flavors()

#=> 9-7
class user():
    def __init__(self,fname,lname,age,height):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.height = height
    def describe_user(self):
        print('First Name: '+self.fname)
        print('Last Name: '+self.lname)
        print('Age: '+str(self.age))
        print('Height: '+str(self.height))
    def greet_user(self):
        print('We welcome you, '+self.fname)

class Admin(user):
    def __init__(self, fname, lname, age, height):
        super().__init__(fname, lname, age, height)
        self.privileges = ['Can Add Post','Can delete Post','Can Ban User']
    def show_privileges(self):
        print('Privileges: '+str(self.privileges))
        
admin = Admin('Shahab','ALi',21,5.8)
admin.show_privileges()



#=> 9-8
class user():
    def __init__(self,fname,lname,age,height):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.height = height
    def describe_user(self):
        print('First Name: '+self.fname)
        print('Last Name: '+self.lname)
        print('Age: '+str(self.age))
        print('Height: '+str(self.height))
    def greet_user(self):
        print('We welcome you, '+self.fname)

class Admin(user):
    def __init__(self, fname, lname, age, height):
        super().__init__(fname, lname, age, height)
        self.privilege = Privileges()

class Privileges():
    def __init__(self,privileges = ['Can add post','Can Delete Post','Can ban User']):
        self.privileges = privileges
    def show_privileges(self):
        print('Privileges: '+str(self.privileges))

admin1 = Admin('Shahab','Ali',21,5.10)
admin1.privilege.show_privileges()

#=> 9-9
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
 
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
 
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.") 
    
    def upgrade_battery(self):
        if self.battery_size==70:
            self.battery_size = 85
            
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
 
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
 
class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
ecar1 = ElectricCar('Tesla','X','2020')
ecar1.battery.get_range()
ecar1.battery.upgrade_battery()
ecar1.battery.get_range()
