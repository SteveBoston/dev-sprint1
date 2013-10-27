from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

bob.delay = .001

def koch(t, x):

	angle = 60

	if x < 3:
		fd(t, x)

	else:
		

		koch(t, x/3)
		lt(t, angle)
		koch(t, x/3)
		rt(t, 2*angle)
		koch(t, x/3)
		lt(t, angle)
		koch(t, x/3)

	
def snowflake(t,x):

	koch(t,x)
	rt(t, 120)
	koch(t,x)
	rt(t, 120)
	koch(t,x)
	



pu(bob)
fd(bob, 400)
rt(bob)
fd(bob, 300)
lt(bob, 90)
pd(bob)


snowflake(bob, 1000)


wait_for_user()
