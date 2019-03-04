__metaclass__ = type


class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print 'Hi,my value is ', self.value


class TalkingCalculator(Calculator, Talker):
    pass


print TalkingCalculator.__class__.__name__
print TalkingCalculator.__bases__
tc = TalkingCalculator()
tc.calculate('2*2*8')
tc.talk()

print hasattr(tc,'talk')
print hasattr(tc,'calculate')
print callable(getattr(tc,'calculate',None))
class ClassOne:
    count = 0

    def __init__(self):
        pass

    def AddCount(self):
        #self.__class__.count += 1
        self.count+=1



a = ClassOne()
a.AddCount()
print a.count
b = ClassOne()
b.AddCount()
print b.count
