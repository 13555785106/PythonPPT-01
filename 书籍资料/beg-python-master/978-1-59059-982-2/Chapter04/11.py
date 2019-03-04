__metaclass__ = type


class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']


f = Filter()
f.init()
print f.filter([1, 2, 3])

s = SPAMFilter()
s.init()
print s.filter(['SPAM','a','b','c','SPAM'])

print issubclass(SPAMFilter,Filter)
print isinstance(s,SPAMFilter)
print isinstance(s,str)
print s.__class__
print SPAMFilter.__bases__