def max_rev(ps, cs):
    return sum(p * c for p, c in zip(ps, cs))

def get_profits_clicks(f):
    with open(f) as f:
        data = [x.strip().split(' ') for x in f]
    profits = sorted(int(x) for x in data[1])
    clicks = sorted(int(x) for x in data[2])
    return (profits, clicks)


if __name__ == '__main__':
    ps, cs = get_profits_clicks('3_3.in')
    print(max_rev(ps, cs))
