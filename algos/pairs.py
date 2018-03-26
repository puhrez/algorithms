import math

def closest_pairs(xs):
    if len(xs) <= 1:
        return Ellipsis

    mid = len(xs) / 2
    left = closest_pair(xs[:mid])
    right = closest_pair(xs[mid:])
    d = min(left, right)

    close_enough = [x for x in xs if abs(x[0] - xs[mid][0]) < d]
    for i, x in enumerate(close_enough):
        for y in close_enough[i + 1:]:
            this_d = distance(x, y)
            if this_d < d:
                d = this_d

    return d

def get_list(f):
    with open(f) as f:
        data = [x.strip().split(' ') for x in f]
    return sorted(((int(x), int(y)) for x, y in data[1:]),
                  key=lambda x: x[0])

def distance(x, y):
    return math.sqrt(
        math.pow(x[0] - y[0], 2) +
        math.pow(x[1] - y[1], 2))
