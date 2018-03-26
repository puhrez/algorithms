def binsearch(xs, low, high, x):
    while low <= high:
        mid = (low + high) / 2
        if xs[mid] == x:
            return mid
        elif xs[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def binsearchr(xs, low, high, x):
    if high <= low:
        return -1
    mid = (low + high) / 2
    if xs[mid] == x:
        return mid
    elif xs[mid] < x:
        return binsearch(xs, mid + 1, high, x)
    else:
        return binsearch(xs, low, mid - 1, x)


def get_list(f):
    with open(f) as f:
        data = [x.strip().split(' ') for x in f]
    entries = sorted(int(x) for x in data[0][1:])
    queries = [int(x) for x in data[1][1:]]
    return entries, queries
