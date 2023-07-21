print("Hello World")

# A comment
# Ask user for their name
name = input("What's your name?:")

# Say hello to user
# function print uses one argument, with a space
# in the quoted text". The + joins the strings and then
# is passed to the function as a single string.
print("Hello," + name)

# Say hello to user
# function print uses two arguments separated by a comma
# and it dynamically inserts a space between each string argument
print("Hello,",name)

############
# Many
# Lines
# Of
# Comments
#############

"""
Three quotes can also be a comment
"""

# Named parameters are optional, and have defaults
# print() default parameters
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# *objects: Can take any number of arguments
# sep=' ': This sets the separator between arguments
# end='\n': Backslash N (\n) means "New Line", tells the cursor to move to the next line


# print to a single line instead of inserting a new line
print("Hello, ", end="")
print(name)

# print another separator
print("Hello,", name, sep='???')

# How to add quotation marks inside other quotes?
#
# Print quotes ""
# Just inserting quotes into a string causes an error
# One solution is to use single quotes wrapped around double quotes
print('Hello, "Friend"')

# Use backslash or "Escape" character to print quotes
print("Hello, \"friend\"")

# Another, newer method
# Use curly brackets around a variable.
# This is called a format, or F string
# inserting an f before the string is a clue to python to format the string
print(f"Hello, {name}")

"""
:45 mins More stuff with Strings
"""