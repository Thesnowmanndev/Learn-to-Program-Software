# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev | This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.

# Indexing from Strings | String Manipulation
# In Python Strings are essentially just a group of characters ordered in a "sequence". Due to that we are able to do 
# various things to manipulate our strings in Python. String Indexing is one of them. 

# Take for example this string:
our_string = "Python Language"

# Every character in a string will have a "key value" or "numeric index" attached to it. In strings the first character
# starts with a 0 and begins to count up or forward. Even "spaces" have a value or index attached to them. So with our 
# string I will list out the index number of each character. P = 0, y = 1, t = 2, h = 3, o = 4, n = 5,  = 6, L = 7, 
# a = 8, n = 9, g = 10, u = 11, a = 12, g = 13, e = 14. In this example we will simply print another word from our 
# string.

def print_other_word():
    new_string = our_string[0] + our_string[7] + our_string[8] + our_string[9] + our_string[14]
    print(new_string.lower())
    
# Essentially we took our original string and used the indexes to create a new string which is "PLane". Then we called
# the print function and within that called the lower function to make the terminal print out plane instead of PLane
# There are many words we can print out just out of our original string. I will name some: pungently, untangle,
# pantheon, anaglyph, pathogen, pentagon, neonatal, analogue, eggplant, outplay, naughty, ethanol, outplan, plateau,
# tangle, tongue, toggle, and many many more. Literally 838 words could be printed out using indexing and our string.

# You can also attach negative index values to our_string. To do this you would start with the last character in the 
# string and label it as -1 and then count down from there with every character. So with our string our negative index
# values would be e = -1, g = -2, a = -3, u = -4, g = -5, n = -6, a = -7, L = -8,  = -9, n = -10, o = -11, h = -12, 
# t = -13, y = -14, and P = -15. Note for negative indexes you do not start at 0 as -0 would not make sense. 

def print_word_using_negatives():
    negative_string = our_string[-15] + our_string[-3] + our_string[-6] + our_string[-13] + our_string[-12] + our_string[-1] + our_string[-11] + our_string[-6]
    print(negative_string.lower())

# IMPORTANT: Create a method named whatever you would like. Inside that method declare a variable and use indexes from
# our_string to create a word. Finally have the method print out your new variable. Don't forget to call it in our main
# function and run it in terminal.


if __name__ == '__main__':
    print_other_word()
    print_word_using_negatives()
