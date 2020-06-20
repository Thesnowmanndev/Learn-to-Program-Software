# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev | This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.


# Our first method in this file creates two variables of type string and assigns them to Hello, and Kyle.
# It then calls a print statement to combine our phrase with our name to complete a message in the terminal.
# See what happens when you remove the " " portion of our first print statement.
# We then call a few additional print statements to print what type those variables.
# Python is a dynamically typed language therefore we do not have to define the type of variable like other languages.


def greeting_with_string_types():
    greet_phrase = "Hello"
    name = "Kyle"
    print(greet_phrase + " " + name)
    print("The greet_phrase variable is of type: ")
    print(type(greet_phrase))
    print("The name variable is of type: ")
    print(type(name))
    print("--- End of Function ---")

# Our next function creates a variable named 'name' and assigns it to the input() function. The input() function will
# wait for user input in the terminal. You can also pass it an argument which we did "Please type your name: ".
# Notice in our greeting we added a space after the word Hello. This prevents us having to add a " " statement in our
# strings that it will be combined with.
# Finally it prints out our greeting and the name that was given. Try it out!


def greeting_custom_name():
    name = input("Please type your name: ")
    greeting = "Hello "
    print(greeting + name)
    print("--- End of Function ---")


if __name__ == '__main__':
    greeting_with_string_types()
    greeting_custom_name()
    print("~~~ End of Application ~~~")


# When you are comfortable with everything in this file feel free to try your hand at these resources:
# https://www.hackerrank.com/challenges/whats-your-name/problem
