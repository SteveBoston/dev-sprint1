# This is where Exercise 5.4 goes
# Name: Steve Gallagher

def is_triangle(a,b,c):
	if c >= a and c >= b and (a + b) >= c:
		print "yes"
	elif b >= a and b >= c and (a + c) >= b:
		print "yes"
	elif a >= b and a >= c and (b + c) >= a:
		print "yes"
	else:
		print "no"

is_triangle(2,3,4)



