#=> 8-1
def display_message():
    print('I am learning about functions in python in this lesson.')
display_message()
print()
#=> 8-2
def favourite_book(title):
    print('One of my favourite books is '+title+'.')
favourite_book('Harry Potter')
print()
#=> 8-3
def make_shirt(size,text):
    print('Shirt Size: '+size+"\nText: "+text)
make_shirt('Small','Helloooo')
print()
size = "Large"
text = "Home"
make_shirt(size,text)
print()
print()

#=> 8-4
def make_shirt(size="Large",text="I Love Python."):
    print('Shirt Size: '+size+'\nMessage: '+text)
make_shirt()
print()
make_shirt('medium')
print()
make_shirt("small","This is small shirt.")
print()
print()
#=> 8-5
def describe_city(name,country='Pakistan'):
    print(name+' is in '+country+'.\n')
describe_city('Lahore')
describe_city('Islamabad')
describe_city('London','UK')

#=> 8-6
def city_country(name,country):
    string = '"'+name+', '+country+'"'+'\n'
    return string
print(city_country('Lahore','Pakistan'))
print(city_country('Rawalpindi','Pakistan'))
print(city_country('Islamabad','Pakistan'))


#=> 8-7
def make_album(artist,title,noOfTracks=0):
    if(noOfTracks!=0):
        album_info = {
            'Artist Name': artist,
            'Album_Title': title,
            'No of Tracks': noOfTracks
        }
    else:
        album_info={
            'Artist Name': artist,
            'Album_Title': title
        }
    return album_info
print(make_album('Ed Sheeran','Perfect'))
print(make_album('Rihanna','XYZ'))
print(make_album('Eminem','8 Mile'))
print(make_album('Imagine Dragon','Demons',20))
print()

#=> 8-12
def sandwiches(*items):
    print(items)
    
sandwiches('Pepporoni')
sandwiches('BBQ','Grilled')
sandwiches('bbq','fajita','Tikka')
print()

#=> 8-13
def build_profile(fname,lname,**user_info):
    profile = {
        'fname':fname,
        'lname':lname,
    }
    for key,value in user_info.items():
        profile[key]=value
    print(profile)
build_profile('Shahab','Ali',age=21,height=5.10)