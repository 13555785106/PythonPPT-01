# -*- coding:utf-8 -*-
score = raw_input('Please input your score:')

score = int(score)
if 60>score>=0:
    print 'E'
elif 100>=score >= 90:
    print 'A'
elif 90>score >= 80:
    print 'B'
elif 80>score >= 70:
    print 'C'
elif 70>score >= 60:
    print 'D'
else:
    print '无效分数'
