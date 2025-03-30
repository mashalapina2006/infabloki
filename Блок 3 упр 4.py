X = 5
target = 2 ** X
L = [2 ** x for x in range(7)]

if target in L:
    print('at index', L.index(target))
else:
    print(X, 'not found')
