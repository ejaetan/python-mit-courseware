from graphics import *

class Block(Rectangle):
	def __init__(self, coords, color):
		upper_left_corner = Point(coords.getX() * 30, coords.getY() * 30)
		lower_right_corner = Point(coords.getX() * 30 + 30, coords.getY() * 30 + 30)
		Rectangle.__init__(self, upper_left_corner, lower_right_corner)
		Rectangle.setFill(self,color)

# Shape class is form by Block class, but not in an inheritance way		
class Shape():
	def __init__(self, coords, color):
		self.blocks = []
		for i in coords:
			self.blocks.append(Block(i,color))
		
	def draw(self, win):
		for block in self.blocks:
			block.draw(win)

class I_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 2, center.y),
				  Point(center.x - 1, center.y),
				  Point(center.x	, center.y),
				  Point(center.x + 1, center.y)]
		Shape.__init__(self, coords, "blue")

class J_shape(Shape):
	def __init__(self,center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x	, center.y),
				  Point(center.x + 1, center.y),
				  Point(center.x + 1, center.y + 1)]
		Shape.__init__(self, coords, "blue")

class L_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x	, center.y),
				  Point(center.x + 1, center.y),
				  Point(center.x - 1, center.y + 1)]
		Shape.__init__(self, coords, "blue")

class O_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x	, center.y),
				  Point(center.x, center.y + 1),
				  Point(center.x - 1, center.y + 1)]
		Shape.__init__(self, coords, "blue")

class S_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x, center.y + 1),
				  Point(center.x	, center.y),
				  Point(center.x + 1, center.y),
				  Point(center.x - 1, center.y + 1)]
		Shape.__init__(self, coords, "blue")
		
class T_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x	, center.y),
				  Point(center.x + 1, center.y),
				  Point(center.x, center.y + 1)]
		Shape.__init__(self, coords, "blue")

class Z_shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x	, center.y),
				  Point(center.x, center.y + 1),
				  Point(center.x + 1, center.y + 1)]
		Shape.__init__(self, coords, 'peach puff')


def main2():
	'''
	win = GraphWin("Tetrominoes", 150, 150)
	block = Block(Point(1,1), 'red')
	block.draw(win)
	
	winI = GraphWin('I-shape', 200, 150)
	shape = I_shape(Point(3,1))
	shape.draw(winI)
	
	winJ = GraphWin('J-shape', 200, 150)
	shape = J_shape(Point(3,1))
	shape.draw(winJ)
	
	winL = GraphWin('L-shape', 200, 150)
	shape = L_shape(Point(3,1))
	shape.draw(winL)
	
	winO = GraphWin('O-shape', 200, 150)
	shape = O_shape(Point(3,1))
	shape.draw(winO)
	
	winS = GraphWin('S-shape', 200, 150)
	shape = S_shape(Point(3,1))
	shape.draw(winS)
	
	winT = GraphWin('T-shape', 200, 150)
	shape = T_shape(Point(3,1))
	shape.draw(winT)
	
	winZ = GraphWin('T-shape', 200, 150)
	shape = Z_shape(Point(3,1))
	shape.draw(winZ)
	'''
	win = GraphWin("Tetrominoes", 900, 150)
	
	# a list of shape classes
	tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]
	x = 3
	for tetromino in tetrominoes:
		shape = tetromino(Point(x,1))
		shape.draw(win)
		x += 4
	
	win.mainloop()

main2()