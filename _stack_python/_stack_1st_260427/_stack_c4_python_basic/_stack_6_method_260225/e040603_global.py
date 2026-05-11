# e040602_scope.py
a = "abc"


def test():
    global a
    a = "def"
    print(a)
    return


test()
print(a)
