Test = type("Test", (), {'age': 13, 'name': "wangbo"})
test1 = Test()
test1.age = 12
print(test1.age)
test2 = Test()
test2.age = 21
print(test2.age)
print(test1.age)
