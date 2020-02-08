def print_numbers(x, y, z):
    print(x, y, z)


if __name__ == '__main__':
    _tuple = (1, 2, 3)
    # _tuple[1] = 6 --> This is not possible because it is inmutable
    tuple_1 = 1, 2, 3
    print(type(tuple_1))
    a = tuple_1[0]
    b = tuple_1[1]
    c = tuple_1[2]
    print(a, b, c)
    x, z, y = tuple_1
    print(x, z, y)
    x, *rest = tuple_1
    print(x)
    print(rest)
    print(*rest)
    print_numbers(*tuple_1)
    print(type(tuple_1))
