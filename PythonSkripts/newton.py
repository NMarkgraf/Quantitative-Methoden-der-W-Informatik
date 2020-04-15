# ========================================================================
# Newton-Verfahren in Python                      Rev. 2.0 (13. Apr 2020)
# ===========================---------------------------------------------
# (C)opyleft in 2020 by N. Markgraf (nmarkgraf@hotmail.com)
#
# ========================================================================

from math import exp, fabs


def print_iter_info(i, x, fx, dfx):
    print(f'Iter. {i}: x={x:.8F} f(x)={fx:.8F} f\'(x)={dfx:.8F}')


def newton(f, df, x_start, max_iter=1000, epsilon=0.0001):
    x = x_start
    for i in range(1, max_iter):
        fx, dfx = f(x), df(x)
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
    print(f'Der x-Wert liegt bei {newton(fkt, dfkt, 4):.10F} \n')
