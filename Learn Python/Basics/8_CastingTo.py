# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev | This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.

# There may be times in your application where you may want to specify a variable as a specific type in order for your
# application to behave how you want it to. We can do this by "Casting".

# Casting in Python:

a = 10
b = 20
c = float(a) 
d = float(b) 

# The variables above are currently ints. Say we want to print a string concatination but not want to hard type the 
# assignments of a and b as it may change from time to time in our application. We can do this by defining what 
# variable type we would like it to be in our expression or line of code. Here is an example of changing it from an 
# int to a string:

def int_to_string():
    print("Our variable 'a' is the value " + str(a))
    print("Our variable 'b' is the value " + str(b))
    
    
# You are also able to cast it to a float or an int. Not just a string. See lines 14 and 15 for an example of changing
# an int into a float. 


def int_to_float():

    print("In decimal format our variable 'a' is the value " + str(c))
    print("In decimal format our variable 'b' is the value " + str(d))
    
    
# Try writing your own method below this comment converting a string into a int or float and run the program to see what 
# happens. Don't forget to call the method in our main function.
    

if __name__ == '__main__':
    int_to_string()
    int_to_float()
