# Secret Messages
# 
# The goal of this exercise is to write a cyclic cipher to encrypt messages. 
# The key idea behind the Caesar cipher is to replace each letter by a letter 
# some fixed number of positions down the alphabet. For example, if we want
# to create a cipher shifting by 3, you will get the following mapping:
# Plain:   ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Cipher:  DEFGHIJKLMNOPQRSTUVWXYZABC
# 
# To be able to generate the cipher above, we need to know how to convert
# char to char code
#
# letter = 'a'
#
# converts a letter to ascii code
# ascii_code = ord(letter)
# 
#
# converts ascii code to a letter
# letter_res = chr(ascii_code)


# Method 1	
encoded_phrase = raw_input("Enter sentence to encrypt: ")
c = input("Enter shift value: ")

# converts string into list (array)
encodedList = list(encoded_phrase)


for i in range (len(encodedList)):
	ascii_code_ori = ord(encodedList[i])
	
	if ( (97 <= ascii_code_ori <= 122 ) or (65 <= ascii_code_ori <= 90 ) ):
		ascii_code = ascii_code_ori + c
	else:
		ascii_code = ascii_code_ori
	
	if ( (97 <= ascii_code_ori <= 122 ) and (ascii_code > 122) ):
		ascii_code -= 123 
		ascii_code += 97
	elif ( (65 <= ascii_code_ori <= 90 ) and ascii_code > 90):
		ascii_code -= 91 
		ascii_code += 65
	
	encodedList[i] = chr(ascii_code)
	

# converts element of list to string
print ''.join(encodedList)

# Method 2
encoded_phrase = raw_input("Enter sentence to encrypt: ")
c = input("Enter shift value: ")
result = ""
for letter in encoded_phrase:
	ascii_code_ori = ord(letter)
	
	if ( (97 <= ascii_code_ori <= 122 ) or (65 <= ascii_code_ori <= 90 ) ):
		ascii_code = ascii_code_ori + c
	else:
		ascii_code = ascii_code_ori
	
	if ( (97 <= ascii_code_ori <= 122 ) and (ascii_code > 122) ):
		ascii_code -= 123 
		ascii_code += 97
	elif ( (65 <= ascii_code_ori <= 90 ) and ascii_code > 90):
		ascii_code -= 91 
		ascii_code += 65
	
	result += chr(ascii_code)
	

# converts element of list to string
print result