# 1. Using a for loop, write a program that prints out the decimal equivalents
# of 1/2, 1/3, 1/4, . . . , 1/10.

for x in range(2, 10):
	print 1/ (x * 1.0)


# 2. Write a program using a while loop that asks the user for a number,
# and prints a countdown from that number to zero. What should your program
# do if the user inputs a negative number? As a programmer, you should always 
# consider edge conditions like these when you program! (Another way to put
# it- always assume the users of your program will be trying to find a way to 
# break it! If you dont include a condition that catches negative numbers,
# what will your program do?)

user_input = input("Please enter a postive number: ")
while (user_input < 0):
	user_input = input("Please enter a postive number: ")


# round and convert user_input into whole number
user_input = int(round(user_input))

while user_input >= 0:
	print user_input
	user_input -= 1


# 3. Write a program using a for loop that calculates exponentials. 
# Your program should ask the user for a base base and an exponent
# exp, and calculate baseexp.

base = input("Please enter a base: ")
exp = input("Please enter an exponent: ")
baseexp = 1

for x in range(0, exp):
	baseexp *= base

print baseexp


# Write a program using a while loop that asks the user to enter a number 
# that is divisible by 2. Give the user a witty message if they enter something
# that is not divisible by 2- and make them enter a new number. Dont let them 
# stop until they enter an even number! Print a congratulatory message when
# they *finally* get it right.

while (1):
	user_input = input("Please enter a number that is divisible by 2: ")

	if(user_input % 2 > 0):
		print "Nope, %d can't be divide by 2." % user_input
	else:
		print "You got it right!"
		exit()	# exit infinite loop
