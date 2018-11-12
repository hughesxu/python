#!/usr/bin/env python

def story(**kwds):
    return 'Once apon a time, there was a '\
            '%(job)s called %(name)s.' % kwds

def power(x, y, *others):
    if others:
        print 'Received redundant parameters:', others
    return pow(x, y)

def internal(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop == None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print internal.__doc__

print story(job = 'king', name = 'Gumby')

params = {'job':'language', 'name':'Python'}
print story(**params)
del params['job']
print params

print story(job='stoke of genius', **params)

params = (5,)*2
print params
print power(*params)
print power(3,3,"hello world")
print internal(10)
print internal(5,10)
print power(*internal(5,10))
