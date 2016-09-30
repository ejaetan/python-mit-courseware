# Name: Yi Jie TAN
# Section:
# hw3.py

##### Template for Homework 3, exercises 3.1 - ######

# **********  Exercise 3.1 ********** 

# Define your function here
def list_intersection(list1, list2):
	result =  [i for i in list1 for j in list2 if i == j]
	# use 'set' to delete duplicated elements
	result = list(set(result))
			
	return result

# Test Cases for Exercise 3.1
print list_intersection([1, 3, 5], [5, 3, 1])
print list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9])
print list_intersection([2, 3], [3,  3,  3,  2, 10])
print list_intersection([2, 4, 6], [1, 3, 5])


# **********  Exercise 3.2 **********
# To figure out if two balls are colliding, we need to compute the distance between their 
# centers, then see if this distance is less than or equal to the sum of their radii. 
# If so, they are colliding

# Define your function here
def ball_collide(ball1, ball2):
	(x1,y1,r1) = ball1
	(x2,y2,r2) = ball2
	
	# compute distance between the centers
	dis = x1 + y1
	# compute sum of radii
	rad = r1 + r2
	
	return dis > rad"

# Test Cases for Exercise 3.2
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True

# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
subject = {"eng": 100, "math": 100, "history": 80}

def add_class(class_name, description):
	subject[class_name] = description
	
# Here, use add_class to add the classes you're taking next term
def print_classes(class_name):
	if subject.has_key(class_name):
		print class_name, '-', subject[class_name]
	else:
		print "No",class_name,"taken"


# Test Cases for Exercise 3.3
add_class("science", 99)
add_class("spanish", 70)
print subject
print_classes("jam")
print_classes('spanish')

# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(l1, l2):
	# use dict(zip to combine two lists into dictionary
    return dict(zip(l1,l2))
    

#print combine_lists(NAMES, AGES)
combined_dict = combine_lists(NAMES, AGES)
print combined_dict

def people(age):
	answer = []
	for key in combined_dict:
		if combined_dict[key] == age:
			answer.append(key)
	return answer
    	

# Test Cases for Exercise 3.4 (all should be True)
print 'Dan' in people(18) and 'Cathy' in people(18)
print 'Ed' in people(19) and 'Helen' in people(19) and\
       'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
print people(21) ==   ['Bob']
print people(22) ==   ['Kelly']
print people(23) ==   []

# **********  Exercise 3.5 **********

def zellers(month, day, year):
    DAYS = { 0: 'Sunday', 1:'Mon', 2:'Tues', 3:'Wed', 4:'Thurs', 5:'Fri', 6:'Sat'}
    MONTHS = {1 :'Jan', 2: 'Feb', 3:'March', 4:'Apr', 5:'May', 6:'June', 7:'July',\
     8:'Aug', 9:'Sept', 10:'Oct', 11: 'Nov', 12:'Dec'}
    
    for i in MONTHS:
    	if MONTHS[i] == month:
    		month = i
    
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
    
    if DAYS[R]:
    	return DAYS[R]


# Test Cases for Exercise 3.5
print zellers("March", 10, 1940) == "Sunday" # This should be True
