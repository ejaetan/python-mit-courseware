# Name: Yi Jie Tan
# Section:
# hw2.py

import math
import random
##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1

def f2(x):
    return x + 1

# **********  Exercise 2.1 ********** 

# Define your function here
##### YOUR CODE HERE #####

def rock_paper_sciss(p1, p2):
	if ( (p1 == 'rock' and p2 == 'rock') or (p1 == 'paper' and p2 == 'paper') or
		 (p1 == 'scissors' and p2 == 'scissors')):
		 print "Tie"
	elif ( (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or
		   (p1 == 'scissors' and p2 == 'paper')):
		   print "Player 1 wins."
	elif ( (p2 == 'rock' and p1 == 'scissors') or (p2 == 'paper' and p1 == 'rock') or
		   (p2 == 'scissors' and p1 == 'paper')):
		   print "Player 2 wins."
	else: 
		print "This is not a valid object selection"

# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####
print 'rock_paper_sciss test case'
rock_paper_sciss('rock','paper');		# return 'Player 2 wins.'
rock_paper_sciss('scissors','paper');	# return 'Player 1 wins.'
rock_paper_sciss('paper','paper');		# return 'Tie'.
# ********** Exercise 2.2 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####
def is_divisible(m, n):
	if (n > 0 and m % n == 0):
		return True
	else:
		return False;

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print 'is_divisible() test case'
print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return? False


# Define not_equal function here
##### YOUR CODE HERE #####

# Test cases for not_equal
##### YOUR CODE HERE #####
def not_equal(a, b):
	if (a == b):
		return False;
	else:
		return True
	
print 'not_equal() test case'	
print not_equal(1, 2)	# should return True
print not_equal(1, 1)	# should return False

# ********** Exercise 2.3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a, b, c):
	return a * b + c
	
print 'multadd() test case'
print multadd(1,2,3)	# return 5
print multadd(1,1,1)	# return 2
print multadd(2,2,2)	# return 6

## 2 - Equations
##### YOUR CODE HERE #####
a = 1
b = math.sin(math.pi/4)
d = math.cos(math.pi/4)
c = d/2

q = math.ceil(276/19.0)
r = 2 * math.log(12, 7)
print 'q: ', q
print 'r: ', r

# Test Cases
angle_test = multadd(a, b, c)
print "sin(pi/4) + cos(pi/4)/2 is:"	# 1.06066017178
print angle_test

ceiling_test = multadd(a,q,r)
print "ceiling(276/19) + 2 log_7(12) is:" # 17.5539788165
print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####
def yikes(x):
	a = 1
	k = math.exp(-x)
	b = x * k
	c = math.sqrt(1 - k)
	return multadd(a, b, c)

# Test Cases
x = 5
print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
	rand_num = random.randint(1, 100)
	print "rand_num: ", rand_num
	return (rand_num % 3 == 0)
	
		
# Test Cases
##### YOUR CODE HERE #####
print 'Test cases for rand_divis_3():'
print rand_divis_3()
print rand_divis_3()
print rand_divis_3()


## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####
def roll_dice(total_die_sides, total_dice_roll):
	for i in range(total_dice_roll):
		rand_num = random.randint(1, total_die_sides)
		print rand_num
		
	print "That's all!"
		
# Test Cases
##### YOUR CODE HERE #####      
print 'Test cases for roll_dice():'                      
roll_dice(6, 3)
roll_dice(100, 2)
roll_dice(1000, 3)

# ********** Exercise 2.5 **********

# code for roots function
##### YOUR CODE HERE #####   
def roots(a, b, c):
	p = math.pow(b, 2)
	t = 4 * a * c
	r = 2 * a
	if ( (p - t > 0) or (p - t == 0) ):
		q = math.sqrt(p - t)
		x1 = (-b + q) / r
		x2 = (-b - q) / r
		print x1, x2
	elif (p - t < 0):
		print 'No real root, its roots are two complex number'
		
# Test Cases
##### YOUR CODE HERE #####   
print 'Test cases for roots():'    
roots(1, -1, 1)		# no real root
roots(5, -1, -3)	# two unequal real roots
roots(9, 42, 49)	# one root