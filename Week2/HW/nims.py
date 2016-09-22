# Name: Yi Jie Tan
# Section:
# nims.py

def play_nims(pile, max_stones):
	while (pile > 0):
		print "pile = %d; max_stones = %d" % (pile, max_stones)
		p1 = -1
		p2 = -1	
		if (p1 < 0):
			while ( (pile >= max_stones) and (p1 < 0 or p1 > max_stones) ):
				p1 = input("Player 1, please enter a number between 0 and max_stones.")
			while ( (p1 < 0 or p1 > pile) and (pile < max_stones) ):
				p1 = input("Player 1, please enter a number between 0 and pile.") 	
			pile -= p1
			if (pile == 0):
				print "P1 won!"
				exit()
				
		print "pile = %d; max_stones = %d" % (pile, max_stones)
		if (p2 < 0):
			while ( (pile >= max_stones) and (p2 < 0 or p2 > max_stones) ):
				p2 = input("Player 2, please enter a number between 0 and max_stones.")
			while (  (p2 < 0 or p2 > pile) and (pile < max_stones) ):
				p2 = input("Player 2, please enter a number between 0 and pile.") 	
			pile -= p2
			if (pile == 0):
				print "P2 won!"
				exit()
			

play_nims(10,2)
play_nims(10,4)
play_nims(20,5)