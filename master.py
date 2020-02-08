

if __name__ == '__main__':

    a = [1, 2, 3]
    print(a)
    print(*a)
    print(type(print(*a)))
    print(type(a))

    # Converting list to tuple
    b = tuple(a)
    print(type(b))
    print(b)

    #  Converting tuple tolist
    z = list(b)
    print(type(z))
    print(z)

    z.append(4)
    print(z)
    z[3] = 5
    print(z)
    z[len(z) - 1] = 6
    print(z)
    z[-1] = 7
    print(z)
    z.pop()
    print(z)
    z.pop()
    print(z)