def max_prizes(n):
    summands = set()
    a = 1
    while n:
        if n - a > a or n - a == 0:
            summands.add(a)
            n -= a
        a += 1
    return summands


if __name__ == '__main__':
    summands = max_prizes(182414564)
    print(len(summands))
    print(list(summands).join(' '))
