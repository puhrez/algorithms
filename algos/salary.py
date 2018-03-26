def max_salary(xs):
    return ''.join(xs)

def get_digits(f):
    with open(f) as f:
        data = [x.strip().split(' ') for x in f][1]
    max_digits = len(max(data))
    digits = sorted(data, key=lambda x: tuple(x[i] if len(x) > i else '9' for i in range(max_digits)),
                    reverse=True)
    return digits

if __name__ == '__main__':
    digits = get_digits('3_6.in')
    print(max_salary(digits))
