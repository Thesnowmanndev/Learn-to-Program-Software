# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.

# Expression: An expression in Python is anything that can be calculated or evaluated to return a value. 
# Read over the code below:


a = 12
b = 3


print(a + b) # Evaluates to 15
print(a - b) # Evaluates to 9
print(a * b) # Evaluates to 36
print(a / b) # Evaluates to 4
print(a // b) # Evaluates to the int version of 4
print(a % b) # Evaluates to 0


print("Our first for loop:")
for i in range(1, a // b):
    print(i)


# A few things to note. First on line 11 the number 12 is an expression as it evaluates to be the literal value of 12
# Second, on line 15 through 20 the a value is an expression as it evaluates to 12, the b value is an expression as it
# evaluates to 3. And the (a + b) or whatever operator it has inside of it is an expression. So expressions in python
# can also contain expressions. 
# Third, in lines 24 & 25 we have 4 expressions. The first is the literal number 1. The second is "a // b". The third 
# expression is "range(1, a //b)". And finally the forth is the "i" on line 25. 
