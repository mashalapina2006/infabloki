my_dict = {
    'banana': 3,
    'apple': 5,
    'orange': 2,
    'kiwi': 4
}

for key in sorted(my_dict.keys()):
    print('{}: {}'.format(key, my_dict[key]))
