#=> 10-6
def sum_num():
    try:
        x = int(input('Enter a number: '))
        y = int(input('Enter a number: '))   
        sum = x + y 
        print(sum)
    except ValueError:
        msg = "Sorry, You did not enter a number."
        print(msg)
        
sum_num()

#=> 10-7
def sumnum_loop():
    while(True):
        try:
            x = int(input('Enter a number: '))
            y = int(input('Enter a number: '))   
            sum = x + y 
            print(sum)
        except:
            continue
#sumnum_loop()

#=> 10-8
def read_file(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read() 
            print(contents)
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
    # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + 
        " words.")
        
filenames = ['cats.txt','dogs.txt']
for filename in filenames:
    read_file(filename)