import numpy

def py_add(a, b):
    c = []
    for i in xrange(0,len(a)):
        c.append(1.324 * a[i] - 12.99 * b[i] + 1)
    return c

def np_add(a, b):
    return 1.324 * a - 12.99 *  b + 1
