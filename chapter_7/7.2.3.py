class Class:
    def method(self):
        print('I have a self')


def function():
    print("I don't...")

instance = Class()
instance.method()

instance.method = function
instance.method()




class Bird:
    song = "Squaawk!"
    def sing(self):
        print(self.song)

bird = Bird()
bird.sing()
birdsong = bird.sing
birdsong()


class Secretive:
    def __inaccessible(self):
        print("you can't see me")

    def _method(self):
        print("with single underscore")

    def accessible(self):
        print("the secret message is :")
        self.__inaccessible()
        self._method()

s = Secretive()
# s.__inaccessible()
s._Secretive__inaccessible() # don't use this

s.accessible()
s._method()
