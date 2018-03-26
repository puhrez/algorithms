import operator as op
from math import inf
from typing import List, Dict, Tuple, Callable

def read_input(f: str) -> Tuple[List[Callable], List[int]]:
    OP_MAP = {
        '+': op.add,
        '-': op.sub,
        '*': op.mul
    }
    with open(f) as f:
        data = [x.strip() for x in f]
    ops = []
    nums = []
    for x in data[0]:
        if not x:
            continue
        elif x.isdigit():
            nums.append(int(x))
        elif x in OP_MAP:
            ops.append(OP_MAP[x])

    return ops, nums


def max_min(ops: List[Callable], i: int, j: int, M: Dict[int, int], m: Dict[int, int]):
    """Merge the max and min from the subexpressions building upto this one"""
    mx = -inf
    mn = inf
    for k in range(i, j):
        print(ops[k],  M[i, k], M[k + 1, j])
        a = ops[k](M[i, k], M[k + 1, j])
        b = ops[k](m[i, k], M[k + 1, j])
        c = ops[k](M[i, k], m[k + 1, j])
        d = ops[k](m[i, k], m[k + 1, j])
        mx = max(mx, a, b, c, d)
        mn = min(mn, a, b, c, d)
    return mx, mn

def expres(ops, nums):
    """
    return the maximum and minimums groupings for each arithmetic operation
    Build up subexpressions until you reach the whole expression
    """
    M, m = init_matrixes(nums)
    nums_len = len(nums)
    i = 0; j = 1
    if len(ops) == 1:
        mx, mn = max_min(ops, i, j, M, m)
        M[i, j], m[i, j] = mx, mn
        return M, m, mx, mn
    # 0,1 1,2 2,3, 3,4, 4,5; 0,2 1,3, 2,4, 3,5; 0,3, 1,4, 2, 5; 0,4, 1,5; 0,5
    for s in range(nums_len):
        print("out")
        for i in range(nums_len - s):
            j = s + i
            if i != j :
                print(i, j)
                mx, mn = max_min(ops, i, j, M, m)
                print(mx, mn)
                M[i, j], m[i, j] = mx, mn
    print_2d_matrix(M, nums, nums)
    print_2d_matrix(m, nums, nums)
    return M, m, M[i, j], m[i, j]


def init_matrixes(nums: List[int]) -> Tuple[Dict[int, int], Dict[int, int]]:
    M = {}
    m = {}
    for i, x in enumerate(nums):
        M[i, i] = x
        m[i, i] = x
        for j in range(len(nums)):
            if i != j:
                m[i, j] = 0
                M[i, j] = 0
    return M, m


def print_2d_matrix(M, rows, cols):
    print('  ', '  '.join(str(cols[i])
                          for i in range(len(cols) )))
    for i in range(len(rows)):
        print(rows[i], [M[i,j] for j in range(len(cols))])
