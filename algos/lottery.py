def lottery(ps, ss):
    ps_ss = sorted(ps + ss,
                   key=lambda x: x[0] if isinstance(x, tuple) else x)
    segs = []
    payouts = 0
    for p_s in ps_ss:
        if isinstance(p_s, tuple):
            segs.append(p_s)
        elif segs:
            # this can be done better
            segs1 = [x for x in segs if p_s < x[1]]
            payouts += len(segs1)
    return payouts

def get_list(f):
    with open(f) as f:
        data = [x.strip().split(' ') for x in f]
    segments = [(int(x), int(y)) for x, y in data[1:-1]]
    points = [int(x) for x in data[-1]]
    return points, segments
