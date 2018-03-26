"""
While alignment distance and edit distance are equivalent problems,
the longest common subsequence problem differentiates itself
become the penalty for not matching is 0.
This is to say, that when building the comparison matrix, i.e.
the matrix that compares every possible prefix of A and B,
if there is no match, it is not "marked" with a +1, except
if they match.

The difference between the comparison matrixes of an alignment matrix
and an edit matrix is that the former subtracks for mismatches/ins/dels and chooses its optimal path based on the max matches
the latter, adding 1 for any operation performed, chooses its optimal based on the minimum operations
"""

def print_2d_matrix(n, m):
    print('  ', '  '.join(str(0) if i == 0 else str(b[i - 1])
                          for i in range(m)))
    for i in range(n):
        print(0 if i == 0 else a[i - 1], [D[i,j] for j in range(m)])

def lcs3(a, b, c):
    D = {}
    for i in range(len(a) + 1):
        D[i, 0, 0] = 0
        for j in range(len(b) + 1):
            D[i, j, 0] = 0
            for k in range(len(c) + 1):
                D[0, j, k] = 0

    for i, x in enumerate(a, 1):
        for j, y in enumerate(b, 1):
            for k, z in enumerate(c, 1):
                if x == y == z:
                    D[i, j, k] = D[i - 1, j - 1, k - 1] + 1
                else:
                    D[i, j, k] = max(D[i, j - 1, k],
                                     D[i - 1, j, k],
                                     D[i, j, k - 1])

    return D, i, j, k

def longest_subseq(a, b):
    D, i, j = alignment_matrix(a, b, sigma=0, mu=0)
    matches = 0
    ins = 0
    dels = 0
    while i and j:
        last = backtrack(D, i, j, sigma=0)
        if last == 'ins':
            i -= 1
            ins += 1
        elif last == 'del':
            j -= 1
            dels += 1
        elif last:
            if last == 'match':
                matches += 1
            i -= 1
            j -= 1

    return matches,mis, ins, dels

def backtrack(D, i, j, sigma=1):
    if not (j or i):
        return
    elif D[i, j] == D[i - 1, j] - sigma:
        return 'ins'
    elif D[i, j] == D[i, j - 1] - sigma:
        return 'del'
    return 'match'

def init_D_A_B(str_a, str_b, sigma=1):
    D = {(0,0): 0}
    A = list(enumerate(str_a, 1))
    B = list(enumerate(str_b, 1))
    for i, _ in A:
        D[(i, 0)] = i * sigma
    for j, _ in B:
        D[(0, j)] = j * sigma
    return D, A, B


def alignment_matrix(str_a, str_b, sigma=1, mu=1):
    D, A, B = init_D_A_B(str_a, str_b, sigma=sigma)
    for i, a in A:
        for j, b in B:
            insertion = D[(i, j - 1)] - sigma
            deletion = D[(i - 1, j)] - sigma
            if a == b:
                match = D[(i - 1, j - 1)] + 1
                choice = max(insertion, deletion, match)
            else:
                mismatch = D[(i - 1, j - 1)] - mu
                choice = max(insertion, deletion, mismatch)
            D[(i, j)] = choice
    return D, i, j

def read_strs(f):
    with open(f) as f:
        data = [x.strip().split() for x in f]
    return list(map(int, data[1])), list(map(int, data[3]))


def read_strs3(f):
    with open(f) as f:
        data = [x.strip().split() for x in f]
    return list(map(int, data[1])), list(map(int, data[3])), list(map(int, data[5]))
