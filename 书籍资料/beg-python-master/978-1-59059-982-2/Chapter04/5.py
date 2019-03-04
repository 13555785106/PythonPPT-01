
__metaclass__ = type
class Person:
    def setName(s, name):
        s.name = name

    def getName(s):
        return s.name

    def greet(s):
        print "Hello,world! I'm %s." % s.name


foo = Person()
print type(foo)
foo.name="Dulj"
print foo.name
foo.greet()
