# Welcome to Learn Python created by Kyle Martin | https://github.com/Thesnowmanndev | This repository is mainly for my
# notes while learning how to program in python. Feel free to read over the files in this repository and learn what
# you can. I will try to leave as detailed notes in a comment form as I can but if you are new to programming dont
# get in the habit of making 100s of comments. Strive to have clean readable code that doesnt require comments to
# explain what it does. That will make you a better developer in the long run.


# Python has many useful escape characters to add more functionality to print statements. These are:
# \' 	= A single quote mark
# \\ 	= A backslash 
# \n 	= Tells the string to print on a new line
# \r 	= Carriage return, functions the same as a new line. (Similar to a carriage return on a typewriter)
# \t    = Tab
# \b    = Backspace
# \f    = Form Feed, This ia a page-breaking control character. Read more in the method below
# \ooo  = Octal Value, ooo represents 3 integers which will result in a octal value of a character
# \xhh  = Hex Value, hh represents 2 alphanumerical characters which will result in a hex value of a char

def single_quote():
    print("1. This is an example of a single quote in a string. Don\'t underestimate it.")
    

def print_backslash():
    print("2. This is an example of printing a backslash in a string. C:\\Users\\")


def new_line():
    print("3. This is an example of printing on a \nnew line.")


def carriage_return():
    print("        This is an example of a carriage return. \r4. See?") 
    # You need to allow the appropriate amount of space for every character after the \r


def tabbed_string():
    print("5. This is an example of a string that \tis tabbed")
    
    
def backspace_string():
    print("6. This is an example of a backspacee\b in a string. See what I did there?")


def form_feed():
    print("7. This is an example of a \f Form Feed in a string.")
    # This is a page-breaking control character which forces the printer to eject the current page printing
    # and continue printing on a new page. It also calls the carriage return function to ensure the printer
    # is printing at the beginning of the page. You will not see anything special when you run this file in
    # terminal


def octal_value():
    print("8. This is an example of a Octal Value String: \110\145\154\154\157 \040\127\157\162\154\144")
    # To test your own values use this simple tool to get the values of characters:
    # https://onlinetexttools.com/convert-text-to-octal or google search 'text to octal'


def hex_value():
    print("9. This is an example of a Hex Value String: \x48\x65\x6c\x6c\x6f \x20\x57\x6f\x72\x6c\x64")
    # You must start the hex value with \x 
    # To test your own values use this simple tool to get the values of characters in hex format:
    # http://www.unit-conversion.info/texttools/hexadecimal/


if __name__ == '__main__':
    single_quote()
    print_backslash()
    new_line()
    carriage_return()
    tabbed_string()
    backspace_string()
    form_feed()
    octal_value()
    hex_value()
