class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self,size):
        self.width, self.height = size
        print "set size, width, height : ", size

    def getSize(self):
        return self.width, self.height


s = Rectangle()
s.height = 100
s.width = 50
print "get size:", s.getSize()
s.setSize((20,80))
print "get size:", s.getSize()



class ProRectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self,size):
        self.width, self.height = size
        print "set size, width, height : ", size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)

p = ProRectangle();
p.height = 100
p.width = 50
print "get size:", p.size
p.size = (20, 80)
print "get size:", p.size

