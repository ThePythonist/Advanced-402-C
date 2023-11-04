import time


def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        runtime = t2 - t1
        print(f"Function {func.__name__} took {runtime} second to execute")

    return wrapper


@tictoc
def solution1():
    c = 0

    for i in range(50000000):
        c += 1

    print(c)


@tictoc
def solution2():
    c = 0

    while c < 50000000:
        c += 1

    print(c)


solution1()
solution2()
