import time


def tictoc(func):
    def wrapper(n):
        t1 = time.time()
        func(n)
        t2 = time.time()
        runtime = t2 - t1
        print(f"Function {func.__name__} took {runtime} second to execute")

    return wrapper


@tictoc
def fibonacci_with_for(n):
    a, b = 0, 1
    fib_list = [a]

    for i in range(n):
        a, b = b, a + b
        fib_list.append(a)

    # print(fib_list)


@tictoc
def fibonacci_with_while(n):
    a, b = 0, 1
    fib_list = [a]

    while len(fib_list) != n:
        a, b = b, a + b
        fib_list.append(a)

    # print(fib_list)


fibonacci_with_while(10000)
fibonacci_with_for(10000)

# for i in range(10):
#     fibonacci_with_while(10000)
#     fibonacci_with_for(10000)
#     print("-" * 150)
