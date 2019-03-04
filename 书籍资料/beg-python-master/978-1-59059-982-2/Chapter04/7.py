__metaclass__ = type


class Bird:
    #    song = 'Squaawk'
    song = 'TTTTTTTT'

    def sing(self):
        print self.song

    def setSong(self, s):
        self.song = s

    def getSong(self):
        return self.song


bird1 = Bird()
# bird1.song='ssssss'
bird2 = Bird()
bird2.song = 'A aa aaa'
bird1.sing()
bird2.sing()


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))