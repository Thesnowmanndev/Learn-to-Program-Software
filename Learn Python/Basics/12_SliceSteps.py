# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev | This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.


# Slicing with Steps | String Manipulation
# So we have learned how to manipulate a string with slicing. Now we can add an additional colon in our square brackets
# and an additional number that represents how many "steps" we want to take at a time. An easy way to picture that is 
# to picture our string as a staircase. Every character represents a "step" on that staircase. In our string the p
# would be step 0, y is step 1, and so on with the ! being step 10 or index 10. Below you will see a series of 
# methods that print out characters in our string but in steps. 

our_string = "Python Fun!"

# Prints out Python Fun!
def one_step():
    print(our_string[0:11:1])
    
# Prints out Python Fun!
def one_step_also():
    print(our_string[0::1])

# Prints out Pto u!
def two_step():
    print(our_string[::2])

# Prints out Ph n
def three_step():
    print(our_string[::3])
    
# Prints out Python
def python_one_step():
    print(our_string[:6:1])
    
# Prints out Pto
def python_two_step():
    print(our_string[:6:2])
    
# Slicing Backwards:
# We are able to use a slice and print it backwards using steps in Python. Here is our string and its index values:
#           1
# 01234567890
# Python Fun!

def string_backwards():
    print(our_string[10:0:-1])
    
# When our method string_backwards() gets ran it will print out our string starting at index 10 up to but not include
# index 0 with 1 index value at a time. You will notice this only prints out "!nuF nohty". The P which is index 0 is 
# not included because the way slicing works. Remember it will slice the string from your start index up to but not 
# include the index you set as the stopping point. Now there is a way to get our entire string to print backwards. 
# Similar to before where we just didn't put a index value the Python interpretor is smart enough to know that we are 
# telling it to print from the end of the string to the begging one step at a time. The method below will print the 
# entire string backwards. 

def full_string_backwards():
    print(our_string[10::-1])
    
# Because we are using a negative value as our step we can essentially omit both the start value and stop value in our
# slice in order to get the entire string to print backwards. 

def full_string_again_backwards():
    print(our_string[::-1])

# You can see this method is identical to our one_step_also() method just backwards.

if __name__ == '__main__':
    one_step()
    one_step_also()
    two_step()
    three_step()
    python_one_step()
    python_two_step()
    string_backwards()
    full_string_backwards()
    full_string_again_backwards()
