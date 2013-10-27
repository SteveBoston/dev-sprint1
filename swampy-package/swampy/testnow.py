from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

bob.delay = 2

def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	fd(t, length*n)
	lt(t, angle)
	draw(t, length, n-1)
	rt(t, 2*angle)
	draw(t, length, n-1)
	lt(t, angle)
	bk(t, length*n)

pu(bob)
fd(bob, 600)
rt(bob)
fd(bob, 300)
rt(bob, 180)
pd(bob)



draw(bob, 30, 0)


