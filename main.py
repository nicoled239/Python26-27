from myFunctions import *

from random import *

turtle.tracer(0)
turtle.colormode(255)
#bob.speed(0)
bob.width(2)
turtle.bgcolor(0, 0, 20)

#random num of polygons with random colors
num = randint(100, 500)

for times in range( num ):
  r = randint(0, 150)
  g = randint(0, 150)
  b = randint(0, 100)
  c= (r,g,b)
  x = randint(-1000, 1000)
  y = randint(-1000, 1000)
  border = randint(5, 30)
  sides = randint (3, 8)
  polygon(sides, 10, c)
  jump(x,y)

#blue to yellow spiral with polygons
jump (0, -70)
for times in range( 256 ):
  c = ( times, times, 100 )
  polygon(4, 350 - times, c )
  bob.forward(10)
  bob.left(10)

#create firework comets
for times in range(11):
  jump(0,0)
  comet2(10,10)
  bob.left(30)

#circles
jump (0,0)
for times in range(100):
       bob.width(1)
       bob.pencolor(times *2, times * 2, 100)
       bob.circle(500)
       bob.left(35)

