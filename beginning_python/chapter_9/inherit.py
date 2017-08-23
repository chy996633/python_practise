class A:

    def __init__(self, name='Andrew'):
        print "I'm constructed, My name is %s" % name

    def hello(self):
        print "Hello, I'm A."

class B(A):
    pass

a = A('Samuel')
b = B()
a.hello()

b.hello()
