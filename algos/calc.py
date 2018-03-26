def greedy_calc(n):
    ops = 0
    nums = [n]
    while n > 1:
        ops += 1
        if not n % 3:
            n /= 3
        elif not n % 2:
            n /= 2
        else:
            n -= 1
        nums.append(n)
    return ops, list(reversed(nums))

def dynamic_Calc(n, pos_ops=None):
    pos_ops = pos_ops or (
        (3, lambda x: x / 3),
        (2, lambda x: x / 2),
        (1, lambda x: x - 1)
    )
    minCalc = {0: -1}
    for i in range(1, n + 1):
        minCalc[i] = Ellipsis
        for num, op in filter(lambda x: not i % x[0], pos_ops):
            # the sub problem here becomes
            # to find the min number of steps (with x operations) to n
            # find the min number of steps
            # among the results
            # of n with those x operations
            steps = minCalc[op(i)] + 1
            if steps < minCalc[i]:
                minCalc[i] = steps
    return minCalc[n]


def get_input(f):
    with open(f) as f:
        data = [x.strip() for x in f]
    return int(data[0])
