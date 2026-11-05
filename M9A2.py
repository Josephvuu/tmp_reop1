# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 9 Assignment 2

starting_string = """Print this in uppercase Print this in lowercase Print this as a title Print this left justified (80 characters, with ='s) Print this right justified (80 characters, with +'s)"""

lines_of_text = ["Print " + p.strip() for p in starting_string.split("Print ") if p]

print(lines_of_text[0].upper())
print(lines_of_text[1].lower())
print(lines_of_text[2].title())
print(lines_of_text[3].ljust(80, '='))
print(lines_of_text[4].rjust(80, '+'))

print(";".join(lines_of_text))

first_j = starting_string.find('j')
second_j = starting_string.find('j', first_j + 1)
print(starting_string[second_j : second_j + 5])