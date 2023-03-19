#Changing, Adding, Removing Items
#Exercise
#==> 3-4
guests = ['Ali','Hamza','Bashir']
print(guests[0]+ ", I am inviting you to dinner.")
print(guests[1]+ ", I am inviting you to dinner.")
print(guests[2]+ ", I am inviting you to dinner.")

print()
print()


#==> 3-5
guests = ['Ali','Hamza','Bashir']
print(guests[0]+ ", I am inviting you to dinner.")
print(guests[1]+ ", I am inviting you to dinner.")
print(guests[2]+ ", I am inviting you to dinner.")

#guest who cant make it
print(guests[0]," can't make it to the dinner.")

guests[0] = 'Qais'

#printing new invitation
print(guests[0]+ ", I am inviting you to dinner.")
print(guests[1]+ ", I am inviting you to dinner.")
print(guests[2]+ ", I am inviting you to dinner.")

print()
print()

#==> 3-6

guests = ['Ali','Hamza','Bashir']
print(guests[0]+ ", I am inviting you to dinner.")
print(guests[1]+ ", I am inviting you to dinner.")
print(guests[2]+ ", I am inviting you to dinner.")

print("Okay! So, I found a bigger dinner table.")
#adding at start
guests.insert(0,'Maluk')
#adding at mid
guests.insert((int(len(guests)/2)), 'Taimoor')
#adding at end
guests.append('Abdullah')
print(guests)

print()
print()

#==> 3-7

guests = ['Ali','Hamza','Bashir']
print(guests[0]+ ", I am inviting you to dinner.")
print(guests[1]+ ", I am inviting you to dinner.")
print(guests[2]+ ", I am inviting you to dinner.")

print("Okay! So, I found a bigger dinner table.")
#adding at start
guests.insert(0,'Maluk')
#adding at mid
guests.insert((int(len(guests)/2)), 'Taimoor')
#adding at end
guests.append('Abdullah')
print(guests)

print("Dinner table wont be available in time and Only two people can be invited.")
print()
#poping the names from the list
removed_guest = ""
removed_guest = guests.pop()
print("Sorry "+removed_guest+" I cannot invite you to dinner.")
removed_guest = guests.pop()
print("Sorry "+removed_guest+" I cannot invite you to dinner.")
removed_guest = guests.pop()
print("Sorry "+removed_guest+" I cannot invite you to dinner.")
removed_guest = guests.pop()
print("Sorry "+removed_guest+" I cannot invite you to dinner.")
print()
print(guests[0]+ ", You are still invited.")
print(guests[1]+", You are still invited")

print()

guests.remove(guests[0])
guests.remove(guests[0])
print(guests)