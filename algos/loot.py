def knapsack(W, v_w):
    val = 0
    while W > 0 and v_w:
        v, w = v_w.pop()
        amount = min(W, w)
        val += amount * calc_v(v, w)
        W -= amount
    return round(val, 4)

def calc_v(v, w):
    return float(v) / w
def get_loot_data(f):
    with open(f) as f:
        a = [x.strip().split(' ') for x in f if x]
        a = [(int(x[0]), int(x[1])) for x in a if x[0]]
    W = a[0][1]
    return W, sorted(a[1:], key=lambda x: calc_v(x[0], x[1]))

if __name__ == '__main__':
    W, v_w = get_loot_data('3_2_loot.in')
    print(knapsack(W, v_w))
