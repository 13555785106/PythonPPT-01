def story(**kwargs):
    return 'Once upon a time,there was a %(job)s called %(name)s.' % kwargs


def power(x, y, *others):
    if others:
        print 'Received redunant parameters:', others
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    print start
    if (stop is None):
        start, stop = 0,start
        print start,stop
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


print story(job='king', name='Gumby')
print story(name='Sir Robin', job='brave knight')
params = {'job': 'language', 'name': 'Python'}
print story(**params)
print power(2, 3)
print power(3, 2)
print power(y=2, x=10)
print power(3, 3, 'Hello,world')

print interval(10)
