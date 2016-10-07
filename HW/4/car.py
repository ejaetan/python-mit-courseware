from graphics import *
from wheel import *

class Car(Wheel):
	def __init__(self, center1, rad1, center2, rad2, rect_height):
		self.first_wheel = Wheel(center1, rad1 * 0.6, rad1)
		self.second_wheel = Wheel(center2, rad2 * 0.6, rad2)
		self.body = Rectangle(Point(center1.getX(), rect_height), \
		center2)
	
	def draw(self,win):
		self.first_wheel.draw(win)
		self.second_wheel.draw(win)
		self.body.draw(win)
	
	def set_color(self, wheels, tires, body):
		self.first_wheel.set_color(wheels, tires)	# inherits Wheel
		self.second_wheel.set_color(wheels, tires)	# inherits Wheel
		self.body.setFill(body)
	
	def animate(self, win, dx, dy, n):
		if n > 0:
			self.first_wheel.move(dx, dy)
			self.second_wheel.move(dx, dy)
			self.body.move(dx, dy)
			win.after(100, self.animate,win, dx, dy, n-1)
		

def main_car():
	# Create a window with width = 700 and height = 300
	new_win = GraphWin("A Car", 700, 300)

	# Create and draw the two wheels and the body
	car1 = Car(Point(50,50), 15, Point(100,50), 15, 40)
	
	# color the wheels grey with black tires, and the body pink
	car1.set_color('black', 'grey', 'pink')
	
	# draw car
	car1.draw(new_win)
		
	# make the car move on the screen
	car1.animate(new_win,1,0,400)

	new_win.mainloop()
	

main_car()
	

