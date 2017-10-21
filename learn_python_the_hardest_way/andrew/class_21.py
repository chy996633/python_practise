def add(a, b):
	print "Adding %d + %d " % (a, b)
	return a + b

def subtract(a, b):
	print "Subtracting %d - %d " % (a, b)
	return a- b

def multiple(a, b):
	print "Multiplying %d * %d " % (a, b)
	return a * b

print "Let's do some math with just functions!"

age = add(30, 5)

height = subtract(175, 5)

weight = multiple(10, 6)

iq  = add(100, 0)

print "Age: %d, Height: %d, Weight: %d, IQ: %d " %  (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.

print "Here is a puzzle."

what = add(age, subtract(height, multiple(weight,multiple(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

