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

spam = 'Hello world'


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        print(spam)
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


class MyClass:

    i = 1       # class variable shared by all instances

    def __init__(self, s):
        print('MyClass.__init__(self, {})'.format(s))

    def f(self):
        self._i = self.i
        print('Hello world', self.i, self._i)        # class variable must be referenced by self.

myClass = MyClass('Hello')
myClass.f()
print(MyClass.i)
