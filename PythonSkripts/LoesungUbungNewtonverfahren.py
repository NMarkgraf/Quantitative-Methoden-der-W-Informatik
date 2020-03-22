from math import exp, fabs


def print_iter_info(i, x, fx, dfx):
    print('%i & %2.8F & %2.8F & %2.8F \\\\ \n' %
          (i, x, fx, dfx))


def newton(f, df, x_start, max_iter=1000, epsilon=1.0 / 1000):
    x = x_start
    for i in range(1, max_iter):
        fx = f(x)
        dfx = df(x)
        print_iter_info(i, x, fx, dfx)
        if abs(fx) < epsilon:
            break
        x = x - (fx / dfx)
    return x


def fkt(x):
    return 100 * x - x ** 2 - (2 * x ** 3 - 25 * x ** 2 + 134 * x + 60)


def dfkt(x):
    return 100 - 2 * x - (6 * x ** 2 - 50 * x + 134)


newton(fkt, dfkt, 2.0, epsilon=0.0000001)
