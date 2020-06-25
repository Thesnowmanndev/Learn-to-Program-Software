# !!!!!!!!!! File in work - Commit incase system failure !!!!!!!!!!
# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev | This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.

# String Operators
# This file shows you how to manipulate a sequence type with operators. There are 5 built in sequence types in Python 3
# and a sequence type is defined as an ordered set of items. Our first sequence type that we will be covering is the string
# type. A string contains items, each being a char. 

greeting = "Hello World!"

# The string above contains 11 items each being the characters H, e, l, l, o, W, o, r, l, d, and  !
# Now that we know the string is above is a sequence type lets manipulate it with operators. First we can concatenate 
# mulitple strings together. For Example:

first_string = "Python is a programming language "
second_string = "that lets you work quickly "
third_string = "and integrate systems more effectively."

def combine_three_strings():
    print(first_string + second_string + third_string)
    

if __name__ == '__main__':
    combine_three_strings()

