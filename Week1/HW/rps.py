# The program should ask the user for input and display the answer as follows:
#  Player 1? rock
#  Player 2? scissors
#  Player 1 wins.
# The only valid inputs are rock, paper, and scissors.
# If the user enters anything else, your program should output an error line.

print "Let's play rock, paper, scissors, please type your answer in lowercase."

p1 = raw_input("Player 1?")
p2 = raw_input("Player 2?")

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