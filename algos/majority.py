from collections import Counter
def majority(xs):
    for x, c in sorted(Counter(xs).iteritems(),
                       key=lambda x: x[1], reverse=True):
        if c > len(xs) / 2:
            return x

def majorityr(xs):
    return _majorityr(xs)[0]

def _majorityr(xs):
    if len(xs) == 1:
        return xs[0], 1
    mid = len(xs) / 2

    lower, l_count = _majorityr(xs[:mid])
    upper, u_count = _majorityr(xs[mid:])

    if lower == upper:
        return lower, u_count + l_count
    elif l_count > u_count:
        return lower, l_count
    elif u_count > l_count:
        return upper, u_count
    return None, 0


def get_list(f):
    with open(f) as f:
        data = [x.strip().split(' ') for x in f]
    return [int(x) for x in data[1]]
