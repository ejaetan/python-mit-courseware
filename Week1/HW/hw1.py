# Name: Yi Jie Tan
# Section: 
# Date: 9/9/2016
# hw1.py

##### Template for Homework 1, exercises 1.2-1.5 ######

print "********** Exercise 1.2 **********"
print "  |  |"
print "--------"
print "  |  |"
print "--------"
print "  |  |"


print "********** Exercise 1.3 **********"

# Do your work for Excercise 1.3 here. Hint - how many different
# variables will you need?
# Answer: I will need two different variables

cell = "  |  |"
line = "--------"
print cell
print line
print cell
print line
print cell


print "********** Exercise 1.4 **********"
print "********* Part II *************"
print "1.", (3 * 5) / (2 + 3)
print "2.", ((7 + 9) ** (1 / 2)) * (2)
print "3.", (4 - 7) ** 3
print "4.", (-19 + 100) ** (1 / 4)
print "5.", 6 % 4


print "********* Part III *************"
a = 10 * 5 + 2
b = 10 * (5 + 2)
print a
print b

print "********** Exercise 1.5 **********"
first = raw_input("Enter your first name: ")
last = raw_input("Enter your last name: ")
print "Enter your date of birth:"
month = raw_input("Month? ")
day = raw_input("Day? ")
year = raw_input("Year? ")

# Chuck  Norris was born on March 10 , 1940.
print first + " " + last + " was born on " + month + " " + day + ", " + year + "."

# Cannot do string concatenation, because some variables aren't string type
# to print different data type in a line, we need to use "," to do it
# Chuck  Norris was born on March 10  , 1940 .
print first, last, "was born on", month, day, ",", year, "."

print "********** Exercise 1.5 **********"
first = raw_input("Enter your first name: ")
last = raw_input("Enter your last name: ")
print "Enter your date of birth:"
month = raw_input("Month? ")
day = input("Day? ")
year = input("Year? ")

print first, last, "was born on", month, day, ",", year, "."

