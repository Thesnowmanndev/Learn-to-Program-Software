# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev | This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.

# String Format Method
# The format() method is a built in method of strings in python. By utilizing it you are able to code methods that have strings 
# inside of them but the strings do not have hardcoded values. They become a lot more fluid and can adapt to what your 
# program may need in certain situations.


mon1 = "January"
mon2 = "February"
mon3 = "March"
mon4 = "April"
mon5 = "May"
mon6 = "June"
mon7 = "July"
mon8 = "August"
mon9 = "September"
mon10 = "October"
mon11 = "November"
mon12 = "December"

# In the method below we utilize the {0} syntax to state that is a placeholder within the string. Once we call the format method
# you can input the value you wish into the string. Notice that the format method only has 1 argument. We defined the only 
# arguement to be the variable age. 
def my_age():
    age = 30
    print("I am {0} years old".format(age))

# In the method below you will notice it is very similar to the method above. Except with this one we have defined 8 arguements
# when calling the format method. Therefore we must put 8 placeholders. Like other languages, when counting you first start at 
# 0 and work your way up. So if we have 8 arguements they will be numbered as 0, 1, 2, 3, 4, 5, 6, and 7. 
# Also you will notice that the print method is split between two lines. This is because in Python it is frowned upon to have lines
# that exceed a certain length.  Just as it is to have tons of comments but I have to relay information somehow in these files
# for you to learn.
def largest_months():
    days = 31
    print("The largest months have {0} days in them and they are {1}, {2}, {3}, {4}, {5}, {6}, and {7}."
    .format(days, mon1, mon3, mon5, mon7, mon8, mon10, mon12))

# You do not have to write a string with formatting indexs in sequential order. Here is an example:
# I believe this is the first time I utilize the triple double quotes in a file. The reason I do that is because it is much easier to 
# have a long string such as the one below and split it up on different lines so its easier to read. Python will recognize that 
# everything between where the """ starts and finishes is one string.
def days_in_months():
        short_months = 28
        normal_months = 30
        long_months = 31
        print("""In a non leap year each month has a certain number of days in it. 
        {3}: {2} 
        {4}: {0} 
        {5}: {2} 
        {6}: {2} 
        {7}: {2} 
        {8}: {1} 
        {9}: {2} 
        {10}: {2}
        {11}: {1}
        {12}: {2}
        {13}: {1}
        {14}: {2}."""
        .format(short_months, normal_months, long_months, mon1, mon2, mon3, mon4, mon5, mon6, mon7, mon8, mon9, mon10, mon11, mon12))
    
if __name__ == '__main__':
    my_age()
    largest_months()
    days_in_months()

