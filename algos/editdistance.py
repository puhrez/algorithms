def edit_matrix(str_a, str_b):
    D, A, B = init_D_A_B(str_a, str_b)
    for i, a in A:
        for j, b in B:
            insertion = D[(i, j - 1)] + 1
            deletion = D[(i - 1, j)] + 1
            if a == b:
                match = D[(i - 1, j - 1)]
                choice = min(insertion, deletion, match)
            else:
                mismatch = D[(i - 1, j - 1)] + 1
                choice = min(insertion, deletion, mismatch)
            D[(i, j)] = choice
    return D, i, j

def init_D_A_B(str_a, str_b):
    D = {(0,0): 0}
    A = list(enumerate(str_a, 1))
    B = list(enumerate(str_b, 1))
    for i, _ in A:
        D[(i, 0)] = i
    for j, _ in B:
        D[(0, j)] = j
    return D, A, B


def edit_distance(str_a, str_b):
    D, i, j = edit_matrix(str_a, str_b)
    return D[(i, j)],


def read_strs(f):
    with open(f) as f:
        data = [x.strip() for x in f]
    return data[0], data[1]
