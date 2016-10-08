from graphics import *

class DigitalClock():
	ampm = 'AM'
	

	def __init__(self, coords, hour, min, sec):
		self.pos = coords	
		self.hour = hour
		self.min = min
		self.sec = sec
		self.test_ampm(hour)
		self.text = Text(coords, str(self.hour % 12) + ':' + str(self.min) +\
					 ':' + str(self.sec) + '' + ampm)
		self.face = Rectangle(Point(coords.x - 115, coords.y - 50),\
		 			Point(coords.x + 110, coords.y + 50))
		self.text.setSize(40)
	
	def draw_text(self, win):
		self.text.draw(win)
		self.text.setFill('MistyRose')

	def draw_face(self, win):
		self.face.setWidth('5')
		self.face.setFill('MediumAquamarine')
		self.face.draw(win)

	
	
	def test_ampm(self, hour):
		global ampm
		if self.hour > 12:
			ampm = 'PM'
		else:
			ampm = 'AM'
		return ampm
	
	
	# call def in class
	# draw call draw_text, draw_face, and update_time
	def draw(self, win):
		self.draw_face(win)
		self.draw_text(win)
		win.after(100, self.update_time, win)
	
	
	def update_time(self, win):
		currTime = self.hour * 3600 + self.min * 60 + self.sec
		currTime += 1
		self.hour = currTime / 3600
		self.min = (currTime % 3600) / 60
		self.sec = (currTime % 3600) % 60
		self.test_ampm(self.hour)
		self.text.setText("%02d" % (self.hour % 12) + ':' + "%02d" % (self.min) +\
					 ':' + "%02d" % (self.sec) + '' + ampm)
		win.after(1000, self.update_time, win)
					 	 

'''
# Text basic
# create the graphics window
new_win = GraphWin("Digital Clock", 300, 300)

# create a text objects centered at (100,100)
msg1 = Text(Point(100, 100), "Hello, world!")
msg1.setSize(20)
msg1.setStyle('bold italic')
msg1.setTextColor('navy')
msg1.draw(new_win)
'''

# create the graphics window
new_win = GraphWin("Digital Clock", 300, 200)

msg2 = DigitalClock(Point(150,100), 13, 30, 23)

msg2.draw(new_win)


# process events
new_win.mainloop()

   