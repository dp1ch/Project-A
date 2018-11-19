#The TurtleBalls By Denis Pichuev
#Project
class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
class Vector:	
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def getX(self):
		return self.x
	def getY(self):
		return self.y	
class Ball:	
	def __init__(self,position,velocity,color,mass):
		self.velocity=velocity
		self.position=position
		self.color=color
		self.mass=mass
	def move(self):
		Oldpositionx=self.position.x
		Oldpositiony=self.position.y
		self.position.x+=self.velocity.x
		self.position.y+=self.velocity.y
		turtle.pu()
		turtle.goto(self.position.x,self.position.y)
		turtle.pd()
		turtle.pencolor(self.color)
		turtle.goto(Oldpositionx,Oldpositiony)
		turtle.pu()
		return self
	def draw(self,bcolor):
		turtle.pu()
		Lcolor=turtle.pencolor()
		
		turtle.pencolor("black")
		turtle.goto(self.position.x,self.position.y-25)
		
		turtle.pencolor(Lcolor)
		turtle.fillcolor(bcolor)
		turtle.begin_fill()
		turtle.pd()
		turtle.circle(25)
		turtle.pu()
		turtle.end_fill()
	def checkBorder(self):
		
		turtle.pencolor("black")
		windowX=500
		windowY=500
		windowY0=-500
		windowX0=-500
		
		if self.position.x+25+self.velocity.x>windowX:
			self.velocity.x*=-1
		if self.position.x-25+self.velocity.x<windowX0:
			self.velocity.x*=-1
		if self.position.y+50+self.velocity.y>windowY:
			self.velocity.y*=-1
		if self.position.y-25+self.velocity.y<windowY0:
			self.velocity.y*=-1
		return self
def CreateList():
	list= []
	
	turtle.pencolor("black")
	for i in range(1):
		list.append(Ball(Point(i*100+100,100),Vector(50,-10),"white",700))
		list.append(Ball(Point(300,200),Vector(-40,-10),"brown",500))
		list.append(Ball(Point(200,200),Vector(40,10),"red",80))
		list.append(Ball(Point(200,300),Vector(-60,+70),"blue",50))
		list.append(Ball(Point(200,150),Vector(-90,+50),"green",100))
		
	return list

def MoveBalls(BallList):
	
		turtle.pencolor("black")
		for i in BallList:
			i=i.checkBorder()
		for i in BallList:
			i=i.move()
		return BallList
def DrawBalls(BallList):
		turtle.pencolor("black")
		turtle.pd()
		for i in BallList:
			turtle.pencolor(i.color)
			i=i.draw(i.color)
		
		turtle.pencolor("black")
def ClearBalls(BallList):
		turtle.pencolor("black")
		turtle.pd()
		for i in BallList:
			i=i.draw("black")
		for i in BallList:
			i=i.draw("black")
		turtle.pu()		
import turtle
turtle.begin_fill()
turtle.pencolor("black")
turtle.pu()
turtle.ht()
turtle.speed(0)
windowX=500
windowY=500
windowY0=-500
windowX0=-500
turtle.setpos(windowX,windowY0)
turtle.pd()
turtle.setpos(windowX,windowY)
turtle.goto(windowX0,windowY)
turtle.goto(windowX0,windowY0)
turtle.goto(windowX,windowY0)
turtle.pd()
turtle.fillcolor("black")
turtle.end_fill()
BallList=CreateList()
while True:
	turtle.pencolor("black")
	turtle.pu()
	BallList=MoveBalls(BallList)
	turtle.pu()	
	DrawBalls(BallList)
	ClearBalls(BallList)


#Frame

#Text

#Picture

#Mark
