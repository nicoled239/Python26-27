import turtle
bob = turtle.Turtle()

#define a fn polygon
def polygon(sides, dist, c):
  angle = 360/sides
  bob.fillcolor(c)
  bob.begin_fill()
  for times in range(sides):        
    bob.forward(dist)
    bob.left(angle)
  bob.end_fill()

#define a fn jump
def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()
  
#define a fn comet
def comet(dist, angle):
    for times in range (10):
        bob.width(times*3)
        bob.fd(dist)
        bob.left(angle)

#define a fn triangle
def triangle (dist, angle):
    for times in range (3):
        bob.fd(dist)
        bob.left(angle)

#define a fn second comet
def comet2 (dist, angle):
  for times in range (11):
    jump(0, 0)
    comet(105, 7)
   
    bob.pencolor("white")
