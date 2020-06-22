# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev | This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.

# Slicing Strings | String Manipulation 
# Continuing on from lesson 10 there is another form of manipulating a string. This is called "Slicing". 

our_string = "Python Language"

def first_slice():
    print(our_string[0:6])

# Using a slice we are able to print out the word Python out of our_string. The 0 represents the starting point,
# and the 6 is the stopping point. Essentially we are telling the application to start at 0 and print out the 
# characters in the string in the indexes up to but not including 6. Also if you start at 0 you can simply just 
# type :6 which means the same thing. Start at the start of the sequence and grab all the characters up to index
# 6. 

def same_first_slice():
    print(our_string[:6])
    
# If you run this script you will see first_slice and same_first_slice print out the same thing. Now lets print out
# Language

def second_slice():
    print(our_string[7:15])
    
# In our string there is technically only 14 indexs but remember we give it a start point and then an end point. If we
# said 14 then we would print from index 7 up to but not including index 14 which is the letter e. Now you could type 
# it the same way we created the method same_first_slice.

def same_second_slice():
    print(our_string[7:])
    
# If you choose to use square brackets for string manipulation you must include at least one colon in the square brackets
# in indicate that you wish to use a slice. Otherwise the computer will return an index. Now lets combine slices. The 
# method below will combine two slices of our original string in order to print a "new string". 

def same_string():
    print(our_string[:5] + our_string[5:])
    
# Now you could print create that method a little different to yield the same result. See the method below. Essentially, by
# providing only a colon in the square brackets we are telling the computer to print the give string at the starting point
# to include the end point

def same_same_string():
    print(our_string[:])
    
    
# Slicing with negative numbers:
# You are able to slice a string with negative numbers as well. However, you cant exactly print "backwards". Instead you would
# just be using the negative index value. For Example:
#           11111
# 012345678901234
# Python Language
# 111111
# 543210987654321
# I know the above segment may be hard to read at first glance but all I did was typed out our_string and then above I placed 
# the positive index numbers and below the string I put the negative index numbers


def slice_negative():
    print(our_string[-8:])
    
    
def doesnt_print():
    print(our_string[-8:-12])
    
# The method doesnt_print() wont print to the terminal as you would think it would. That is because we can not slice a name and 
# print backwards. If we could, that method would print out "L no" in our_string but python does not allow slices to work like 
# that. 
    

if __name__ == '__main__':
    print(our_string)
    first_slice()
    same_first_slice()
    second_slice()
    same_second_slice()
    same_string()
    same_same_string()
    slice_negative()
    doesnt_print()
