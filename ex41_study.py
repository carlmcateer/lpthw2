class X(Y)
# Make a class named 'X' that is a 'Y'

class X(object):
    def __init__(self, J):
# class X has-a __init__ that takes self and J as parameters.

class X(object):
    def M(self, J):
# class X has-a function named M that takes self and J as parameters.

foo = X()
# set foo to and instance of class X.

foo.M(J)
# from foo get the M function, call it with parmaeters self, J.

foo.K(Q)
# from foo get the K attribute, and set it to Q.
