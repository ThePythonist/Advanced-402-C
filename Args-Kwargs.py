def func1(*args):
    args = list(args)
    print(args)


func1(10,20,30)


def func2(**kwargs):
    print(kwargs)


func2(teacher="sadeghi", students=["matin", "hesam", "mayam", "homayon"])
