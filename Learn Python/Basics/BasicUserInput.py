# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.

# This file is to teach you how to deal with user input. Here we ask the user what their name is and then we print
# their name back out to them with a greeting. 
# First we create a method named user_name_input and pass it two variable arguments named first_name, and last_name
# Second we call the print function passing it a concatenated string with the variables passed to the method


def user_name_input(first_name, last_name):
    print("Hello " + first_name + ' ' + last_name + '.')


# Next we create the main function. 
# Inside the main function we create the two variables first_name and last_name and assign it to the raw_input function
# Within the raw_input functions we pass it a string argument.
# Finally we call the user_name_input method and pass it our two created variables. Run it and see what happens.


if __name__ == '__main__':
    first_name = raw_input("What is your first name? ")
    last_name = raw_input("What is your last name? ")
    user_name_input(first_name, last_name)


# Change the raw_input functions to input functions and see what happens. Once that is done look up the error given by
# the terminal on google and learn why we would use raw_input over input function for this application.
