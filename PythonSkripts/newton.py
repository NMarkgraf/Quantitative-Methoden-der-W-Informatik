# ========================================================================
# Newton-Verfahren in Python                       rev. 1.0 (22.Mrz 2020)
# ===========================---------------------------------------------
# (C)opyleft in 2020 by N. Markgraf (nmarkgraf@hotmail.com)
#
# ========================================================================

from math import exp, fabs


def print_iter_info(i, x, fx, dfx):
    print('Iter. %i: x=%2.8F f(x)=%2.8F df(x)=%2.8F \n‚' %
          (i, x, fx, dfx))


def newton(f, df, x_start, max_iter=1000, epsilon=1.0/1000):
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
    return -x**3+8*x**2-9*x-18


def dfkt(x):
    return -3*x**2+16*x-9


if __name__ == "__main__":
    print('Der x-Wert liegt bei %2.8F \n' % (newton(fkt, dfkt, 4)))
