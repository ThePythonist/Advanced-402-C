# def increase(x):
#     return x + 1
#
#
# def decrease(x):
#     return x - 1
#
#
# def operate(func, x):
#     result = func(x)
#     return result
#
#
# print(operate(decrease, 5))


def prettier(func):
    def wrapper():
        print("----------------")
        func()
        print("----------------")

    return wrapper


# def say_hello():
#     print("Hello!")
#
#
# d = decorator(say_hello)
# d()


@prettier
def say_hello():
    print("Hello!")


say_hello()
