from typing import Tuple, List, Dict

def knapsack(W: int, items: Tuple[int, int]):
    """Fill a knapsack of W optimally with items of (weight, value)"""
    M = init_matrix(W, items)
    for i, item in enumerate(items, 1):
        for wei in range(W + 1):
            M[wei, i] = max(
                M[wei, i - 1],
                M[wei - item[0], i - 1] + item[0]
            ) if item[0] <= wei else M[wei, i - 1]
    return M, W, i

def init_matrix(W: int, items: List[Tuple[int, int]]) -> Dict[int, int]:
    M = {(0, 0): 0}
    for w in range(1, W + 1):
        M[w, 0] = 0
    for i, _ in enumerate(items, 1):
        M[0, i] = 0
    return M

def read_inputs(f: str) -> Tuple[int, List[Tuple[int, int]]]:
    """from `f` returns (W, items)"""
    with open(f) as f:
        data = [x.strip().split() for x in f]
    return int(data[0][0]), [(int(x), 1) for x in data[1]]
