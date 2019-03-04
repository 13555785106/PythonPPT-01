__metaclass__ = type


class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1

    @staticmethod
    def printMe():
        print MemberCounter.members


m1 = MemberCounter()
m1.init()
m1.members = "Two"
print m1.members
m1.printMe()
print MemberCounter.members


m2 = MemberCounter()
m2.init()
m2.members = "er"
print m2.members
print MemberCounter.members
