#!/usr/bin/env python

count = 1
def binary_search(sequence, number, left, right):
    global count 
    print 'times : %d' % count
    if left == right:
        assert number == sequence[left]
        return left
    else:
        middle = (left + right) // 2
        if number < sequence[middle]:
            return binary_search(sequence, number, left, middle-1)
        elif number > sequence[middle]:
            return binary_search(sequence, number, middle+1, right)
        else:
            return middle

seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print seq
binary_search(seq, 67, 0, len(seq))
