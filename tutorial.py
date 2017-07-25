l = [1, 2, 3]

for i in l:
    if i % 2 == 0:
        break
else:
    print('Normal finish 1')

for i in l:
    pass
else:
    print('Normal finish 2')


def test():
    """A function to test function definition."""
    print('The global variable can be referred:', l[1])

test()
