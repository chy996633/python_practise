def checkIndex(key):
    """
    is the key a acceptable index ?
    In order to be accepted, the key should be a non-negative integer.
    """

    if not isinstance(key, (int, long)): raise TypeError
    if key < 0: raise IndexError

class ArithmeticSequence:
    def __init__(self, start = 0, step = 1):
        """
        initialize the sequence.
        """

        self.start = start
        self.step = step
        self.changed = {}

        print "this sequence start from %d, step is %d" % (start, step)

    def __getitem__(self, key):
        checkIndex(key)

        try: return self.changed[key]
        except KeyError:
            return self.start + self.step * key

    def __setitem__(self, key, value):
        checkIndex(key)

        self.changed[key] = value;
        print "s[%d] has been set %s" % (key, value)




s = ArithmeticSequence(1,2)
print "s[4] is ", s[4]
s[5] = -9
print "s[5] is ", s[5]
print s['notExist']
print s[-8]


