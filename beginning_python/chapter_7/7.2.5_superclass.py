class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class NumberFilter(Filter):
    def init(self):
        self.blocked = range(100)


f = NumberFilter()
f.init()
print(f.filter([1, 2, "Samuel", "1231",1.23234, True, False ]))

