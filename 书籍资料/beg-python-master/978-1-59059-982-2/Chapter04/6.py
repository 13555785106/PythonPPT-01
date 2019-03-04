__metaclass__ = type
class Class:
    def method(self):
        print 'I have a self!'


def function():
    print "I don't..."


instance = Class()
print type(instance)
instance.method()
instance.method = function
instance.method()
