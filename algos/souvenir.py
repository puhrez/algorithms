from typing import List, Dict

def read_inputs(f: str) -> List[List[int]]:
    with open(f) as f:
        data = [x.strip().split() for x in f]
    return [[int(x) for x in l] for l in data[1::3]]


def souvenirs_partionable(n: int, xs: List[List[int]]) -> int:
    """
    Return 0 if xs can not be split into n equitable sums
    An optimal solution is a sum that is equal to the sum of equitable subdivision, answer = sum(xs) / n
        An optimal subsolution for elements up to i of xs is one that's a sum equal to equitable subdivisons up to i, answer = sum(xs - i) / n
    After the sanity assertions, we know the following about xs:
        every element is <= to sum(xs) / n (no one element is worth more than an allowed portion)
        there are atleast n elements (atleast one per n)
        sum(xs) is cleanly divisible by n
    So what are we limiting for, i.e. what are we building up for? Sums up to sum(xs) / n. If the our final sum is equal to sum(xs) / n, then the list is partionable
    """
    ssum = sum(xs)

    if ssum % n \
       or len(xs) < n \
       or any(x > ssum / n for x in xs):
        return {(0, 0): 0}, 0, 0, False
    ssum = int(ssum / n)
    M = init_matrix(xs, ssum)
    for i, x in enumerate(xs, 1):
        for s in range(ssum + 1):
            # if x is bigger than this subsum
            if s - x < 0:
                # don't add it, keep current sum
                M[s, i] = M[s, i - 1]
                continue
            val = M[s - x, i] + x
            # if adding this is less than or equal to an even sum
            if val <= ssum:
                # add it
                M[s, i] = val
            else:
                # other wise, don't keep curreent sum
                M[s, i] = M[s, i - 1]
    return M, i, s, M[s, i] == ssum

def init_matrix(xs: List[List[int]], ssum: int) -> Dict[int, int]:
    M = {(0, 0): 0}
    for x in range(ssum + 1):
        M[x, 0] = 0
    for x in range(len(xs) + 1):
        M[0, x] = 0
    return M

def get_answers(inputs, n):
    res = []
    for xs in inputs:
        M, i, y, r = souvenirs_partionable(n, xs)
        res.append(r)
    return ''.join(
        ['1' if r else '0' for r in res]
    )
