def min_visits(xs):
    start = xs[0][1]
    segs = {start}
    for x in xs:
        if not (start >= x[0] and start <= x[1]):
            segs.add(x[1])
            start = x[1]
    return segs


def get_segments(f):
    with open(f) as f:
        data = [x.strip().split(' ') for x in f]
    segs = [(int(x[0]), int(x[1])) for x in data[1:] if x[0]]
    return sorted(segs, key=lambda x:(x[1], x[0]))

if __name__ == '__main__':
    segs = get_segments('3_4.in')
    print(len(segs))
    print(list(min_visits(segs)).join(' ') + '\n')
