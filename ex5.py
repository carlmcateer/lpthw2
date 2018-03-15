name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teath = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "In Ireland that would be %f cm tall." % (height * 2.54)
print "He's %d pounds heavy." % weight
print "And for the Irish again thats %f kilo's." % (weight * 0.453592)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teath are usually %s depending on the coffee" % teath

# This line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d" % (
age, height, weight, age + height + weight
)
