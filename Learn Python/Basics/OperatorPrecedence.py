# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev | This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.

# OPERATOR PRECEDENCE:
# In Python, like other languages, operators do have precedence. Depending on which country you are from and how you
# were taught to perform mathematics you will be fimiliar with these Operator Precedence Acronyms. For example, I was 
# taught math in the US so I am fimiliar with the PEMDAS acronym. However I want you to know that you will see I 
# listed them in Tiers. If they are in the same tier then they are on level ground with each other. For example, 
# in tier 4 addition does not take precedence over subtraction or vice versa. 

# PEMDAS - (Tier 1: Parentheses)(Tier 2: Exponents)(Tier 3: Multiplication & Division)(Tier 4: Addition & Subtraction)
# BEDMAS - (Tier 1: Brackets)(Tier 2: Exponents)(Tier 3: Division & Multiplication)(Tier 4: Addition & Subtraction)
# BODMAS - (Tier 1: Brackets)(Tier 2: Order)(Tier 3: Division & Multiplication)(Tier 4: Addition & Subtraction)
# BIDMAS - (Tier 1: Brackets)(Tier 2: Index)(Tier 3: Division & Multiplication)(Tier 4: Addition & Subtraction)

# Here is an example of a mathematical expression: This will print out 35.0.


a = 12
b = 3
print(a + b / 3 - 4 * 12)


# One thing I would like you take notice of is how it may be clear to the computer but not the developer by just 
# reading the line. You can use parentheses in your expressions where you see fit to make your code more readable
# by other developers. 

print(a + (b / 3) - (4 * 12))

# To me that seems much more readable than the first one just by a glance. 