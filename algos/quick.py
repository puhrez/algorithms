from random import randint

def quicksort(xs):
    """grabs a pivot element, and sorts the thigns before/after"""
    if len(xs) <= 1:
        return
    r = len(xs)
    l = randint(0, r - 1)
    m1, m2 = partition(xs, l, r)
    quicksort(xs[:m1])
    quicksort(xs[m2:])

def partition(xs, l, r):
    """returns the final positions range of the elem at xs[l]"""
    j = l
    x = xs[l]
    for i in range(l + 1, r):
        if xs[i] < x:
            xs[j], xs[i] = xs[i], xs[j]
            j += 1
        elif xs[i] == x:
            xs[l] = xs[i]
            l += 1
    xs[j] = x
    return j, l

def get_list(f):
    with open(f) as f:
        data = [x.strip().split(' ') for x in f]
    return [int(x) for x in data[1]]
