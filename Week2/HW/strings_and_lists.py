# Name: Yi Jie TAN
# Section:
# strings_and_lists.py

# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    # number_list is a list of numbers
	for x in range(len(number_list)):
		temp = x;
		while (temp > 0):
			number_list[x] = number_list[x] + number_list[temp - 1]
			temp -= temp
		if (x == len(number_list) - 1 ):	
			return number_list
   

# Test Cases
print "cumulative_sum of [4,3,6]:", cumulative_sum([4,3,6]) # [4, 7, 13]
print "cumulative_sum of [2,3,5]:", cumulative_sum([2,3,5]) # [2, 5, 10]
print "cumulative_sum of [1,2,3]:", cumulative_sum([1,2,3]) # [1, 3, 6]

# **********  Exercise 2.8 **********

def report_card():
    ##### YOUR CODE HERE #####
    classes = input("How many classes did you take? (in number) ")
    my_list = []
    gpa = 0.0
    for x in range(classes):
    	class_name = raw_input("What was the name of this class? ")
    	grade = raw_input("What was your grade (in number)? ")
    	my_list.append(class_name + " - " + grade)
    	gpa += int(grade)
    
    print "..."
    print "REPORT CARD: "
    
    for i in my_list:
    	print i


	print "Overall GPA %.2f" %(gpa /= len(my_list))
	
# Test Cases
## In comments, show the output of one run of your function.
report_card()

# **********  Exercise 2.9 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
	if (word[0] in VOWELS):
		return word + "hay"
	else:
		return word[1:] + word[0] + "ay"
		 
    

# Test Cases
##### YOUR CODE HERE #####
print pig_latin("ello")		# ellohay
print pig_latin("mellon")	# ellonmay
print pig_latin("fish")		# ishfay


# **********  Exercise 2.10 **********
# 1. Write a list comprehension that prints a list of the 
# cubes of the numbers 1 through 10.
print [x**2 for x in range (1,11)]


# 2. Write a list comprehension that prints out the possible
# results of two coin flips (one result would be ht)
print [x+y for x in ['h','t'] for y in ['h','t']]

# 3. Write a function that takes in a string and uses a 
# list comprehension to return all the vowels in the string.
def list_comp(word):
	word = word.lower()
	return [x for x in word if x in ['a','e','i','o','u']]
	
print list_comp("HELLO") # ['e', 'o']
print list_comp("love")	# ['o', 'e']
print list_comp("miss")	# ['i']


# 4. Run this list comprehension in your prompt:
#     [x+y for x in [10,20,30] for y in [1,2,3]]
# Figure out what is going on here, and write a nested for loop
# that gives you the same result. Make sure what is going on makes sense to you!
# x1 + y1, x1 + y2, x1 + y3
# x2 + y1, x2 + y2, x2 + y3
# x3 + y1, X3 + y2, x3 + y3
print [x+y for x in [10,20,30] for y in [1,2,3]] 
#[11, 12, 13, 21, 22, 23, 31, 32, 33]


list = []
for x in [10,20,30]:
	for y in [1,2,3]:
		list.append(x + y)

print list


# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 
VOWELS = ['a', 'e', 'i', 'o', 'u']
SPECIAL = ['th', 'st', 'qu', 'pl', 'tr']

def pig_latin_complex(word):
	if (word[0] in VOWELS):
		return word + "hay"
	elif (word[0] + word[1] in SPECIAL):
		return word[2:] + word[0] + word[1] + "ay"
	else:
		return word[1:] + word[0] + "ay"
		

def pig_latin_sentence():
	new_word_list = []
	phrase = raw_input("Enter a sentence only with words and spaces:\n")
	phrase.lower()
	word_list = phrase.split()
	
	for x in word_list:
		new_word_list.append(pig_latin_complex(x))
	
	print " ".join(new_word_list)	# merge all element of list and form a sentence
	

pig_latin_sentence()	

# **********  Exercise OPT.2 **********

# 1. Write a function that takes in a list of elements of different types and 
# uses a list comprehension to return all the elements of the list of type int.
# Note: The function isinstance will be of help here. Google Python isinstance
# and see if you can figure out what it does, or type help(isinstance) at the
# Python shell.

def check_list_type(list):
	result = []
	for x in list: 
		if isinstance(x, int):
			result.append(x)
	
	return result

print check_list_type([1,2,3,'a','b','c'])


# 2. Write a list comprehension which solves the equation y = x^2 + 1. 
# Your solution should print out a list of [x, y] pairs; 
# use the domain x ∈ [−5, 5] and the range y ∈ [0, 10].
print [(x,y) for x in range(-5,5) for y in range (0,10) if y == x**2 + 1]

# 3. Similarly, write a list comprehension that finds the integer solutions [x, y] 
# for a circle of radius 5.
print [ (x,y) for x in range(-5, 5) for y in range(-5, 5) if x**2 + y**2 == 25 ]

