# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev | This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.

# Python Basic Arithmetic Operators
# Operator          Description   
# + Addition        Adds values on either side of the operator
# - Subtraction     Subtracts right hand operand from left hand operand
# * Multiplication  Multiplies values on either side of the operator
# / Division        Divides left hand operand by right hand operand 
# % Modulus         Divides left hand operand by right hand operand and returns the remainder 
# ** Exponent       Performs exponential (power) calculation on operators
# // Floor Division Rounds a double down into an int

# Examples:
a = 10
b = 20


def addition():
    result = a + b
    print(str(a) + " + " + str(b) + " equals " + str(result))


def subtraction():
    result = a - b
    print(str(a) + " - " + str(b) + " equals " + str(result))


def multiplication():
    result = a * b
    print(str(a) + " * " + str(b) + " equals " + str(result))


def division():
    result = b / a
    print(str(b) + " / " + str(a) + " equals " + str(result))


# If you have changed the values of a and b above the modulus method below may not be correct with the strings I 
# wrote. Keep that in mind. This method assumes a = 10 and b = 20. If you are confused about the modulus operator
# watch this video as it helped me understand it better: https://www.youtube.com/watch?v=b5cb_nfDyyM or
# https://www.youtube.com/watch?v=pNXwzIohx8c
def modulus():
    result = b % a
    print(str(a) + " goes into " + str(b) + " exactly 2 times with nothing left over.")
    print("So the remainder left over is " + str(result))


def exponent():
    result = b ** a
    print(str(b) + " to the power of " + str(a) + " equals " + str(result))
    
   
# Floor Division rounds down.   
def floor_division():
    c = 10.5
    d = 2.0
    result = c // d
    print(str(c) + " divided by " + str(d) + " is " + str(result))


if __name__ == '__main__':
    addition()
    subtraction()
    multiplication()
    division()
    modulus()
    exponent()
    floor_division()
