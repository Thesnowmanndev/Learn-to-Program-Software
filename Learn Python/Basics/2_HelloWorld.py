# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev | This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.


# This is the traditional "first program" when learning how to program in a language. You are not required to code it
# yourself but I do encourage you to read over this file.
# Below you see the function "hello_world". Functions start with "def" which means definition. Your functions must
# have a name that follows the 'def' keyword. Python has fairly strict naming conventions. A function must begin
# with a letter (uppercase or lowercase) or a underscore. It cannot begin with a number.

# The function 'hello_world' contains one statement of type print.
# The print statement contains a string "Hello, World!".
# Strings must be contained by either double (") quote marks, single (') quote marks, or triple double (""") quote marks
# More on strings in the String.py file.


def hello_world():
    print("Hello, World!")

# Below you see the main method. This is where your program will look first in order to run. You can see in our
# main method we simply call the hello_world function.
# Run the main method and see what happens.


if __name__ == '__main__':
    hello_world()


# When you have memorized or think you are comfortable with this file feel free to head over to these resources:
# https://www.hackerrank.com/challenges/py-hello-world/problem
