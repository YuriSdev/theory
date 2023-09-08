my_str = 'that a string man test'

# Method 1
# The first word of a string
print('method 1: ' + my_str.capitalize())

# Method 2
met2 = my_str[0].upper() + my_str[1:]
print('method 2: ' + met2)

# Method 3
print('method 3: ' + my_str.title())

# Split a string by single words
print(my_str.split())

# Remove spaces
print(my_str.replace(" ", ""))


def my_result(txt):
    txt = txt.title()
    txt = txt.replace(" ", "")
    print(txt)


# my_result(input("Test script name: "))

# Remove whitespaces strip() functions
def check_strip(txt):
    print(txt.strip())
    print(txt.lstrip())
    print(txt.rstrip())


check_strip(" that a text ")


# count return the number of times a substring appears in a string
# how many characters appear in a string etc
def check_count(txt, subtext):
    print(txt.count(subtext))


check_count("some test test string", "test")


# is a string ends with a substring
def check_endswith(txt, subtext):
    print(txt.endswith(subtext))


check_endswith("my text", "text")


# check is a string contains only numeric values
def check_numeric(txt):
    print(txt.isnumeric())


check_numeric("134324")


# formating string

example = "format() method"
formatted_string = "this is an example of using the {} on a string".format(example)
print(formatted_string)

first = "apple"
second = "banana"
third = "carrot"
formatted_string = "{0} {2} {1}".format(first, second, third)
print(formatted_string)

