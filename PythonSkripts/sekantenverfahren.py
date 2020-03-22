# ========================================================================
# Sekantenverfahren in Python                       rev. 1.0 (22.Mrz 2020)
# ===========================---------------------------------------------
# (C)opyleft in 2020 by N. Markgraf (nmarkgraf@hotmail.com)
#
# ========================================================================

from math import exp, fabs


def print_iter_info(i, x, fx, dfx):
    print('Iter. %i: x=%2.8F f(x)=%2.8F Delta f(x)=%2.8F' %
          (i, x, fx, dfx))


def sekantenverfahren(f, x_0, x_1, max_iter=1000, epsilon=1.0/1000):
    x_last = x_0
    x_cur = x_1
    fx = f(x_last)
    for i in range(1, max_iter):
        fxl = fx
        fx = f(x_cur)
        dfx = (fxl - fx) / (x_last - x_cur)
        print_iter_info(i, x_cur, fx, dfx)
        if abs(fx) < epsilon: 
            break
        x_last = x_cur
        x_cur = x_last - (fx / dfx)
    return x_cur


def fkt(x):
    return -x**3+8*x**2-9*x-18


if __name__ == "__main__":
    print('Der x-Wert liegt bei %2.8F \n' %
          (sekantenverfahren(fkt, 2, 4, epsilon=0.0000001)))
