

if __name__ == '__main__':

    a = [1, 2, 3, 4]
    b = a[:3] # slicing
    c = [a[x] for x in range(len(a) - 1)]  # [a[0], a[1], a[2]]
    print(c)
    people = {
        'sinan': 'Turkey',
        'daniel': 'spain',
        'laura': 'Italy'
    }
    print(people['daniel'])
    people['helene'] = 'France'
    print(people)
    for name, city in people.items():
        print(name, city)

    world_people = {'sinan', 'daniel', 'laura', 'sinan'}
    w = set(['sinan', 'daniel', 'laura'])
    print(world_people)
    print(w)
    french_people = {'helene'}
    no_french = world_people - french_people
    print(no_french)
    aliens = {'mars'}
    everyone = world_people | aliens
    print(everyone)
    print(sorted(list(everyone)))
