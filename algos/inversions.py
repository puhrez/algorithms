def mergesort(xs):
    if len(xs) <= 1:
        return xs, 0
    mid = len(xs) / 2
    lower, l_c = mergesort(xs[:mid])
    upper, u_c = mergesort(xs[mid:])
    merged, m_c = merge(lower, upper)
    return merged, m_c + u_c + l_c

def merge(a, b):
    res = []
    invs = 0
    len_a = len(a)
    l = 0
    while a and b:
        if a[0] <= b[0]:
            res.append(a[0])
            del a[0]
            l += 1
        else:
            res.append(b[0])
            ## this important because for every moment that
            ## the head of b is less than the head of a
            ##  the head of b is also less every x remaining in a
            ## doing this afterward, will only account for inversions
            ## of the elements of a that are larger than every b,
            ## not some b which is what is needed.
            invs += (len_a - l)
            del b[0]

    if a:
        res += a
    else:
        res += b

    return res, invs

def get_list(f):
    with open(f) as f:
        data = [x.strip().split(' ') for x in f]
    return [int(x) for x in data[1]]
