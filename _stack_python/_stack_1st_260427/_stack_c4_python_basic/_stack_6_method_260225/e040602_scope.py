# e040602_scope.py
a = "abc"


def test():
    a = "def"
    print(a)
    return


test()
print(a)
