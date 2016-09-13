# Zeller's Algorithm
# 
# Zeller's algorithm computes the day of the week on which a given date will 
# fall (or fell). In this exercise, you will write a program to run Zeller's 
# algorithm on a specific date. The program should use the algorithm outlined
# below to compute the day of the week on which the user's birthday fell in 
# the year you were born and print the result to the screen.

print "Let's find out the day of the week when you're born."
print "Enter your date of birth:"
month = input("Month? (in number, eg: 3 for March) ")
day = input("Day? ")
year = input("Year? ")

if (3 <= month <= 12):
	A = month - 2

B = day

if (month == 1 or month == 2):
	A = 10 + month
	C = (year % 100) - 1
else:
	C = year % 100

D = year / 100

W = (13 * A - 1) / 5
X = C / 4
Y= D / 4
Z = W + X + Y + B + C - 2 * D
R = Z % 7

if R == 0:
	print "You're born on a Sunday."
elif R == 1:
	print "You're born on a Monday."
elif R == 2:
	print "You're born on a Tuesday."
elif R == 3:
	print "You're born on a Wednesday."
elif R == 4:
	print "You're born on a Thursday."
elif R == 5:
	print "You're born on a Friday."
elif R == 6:
	print "You're born on a Saturday."



