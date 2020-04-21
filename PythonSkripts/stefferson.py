# ========================================================================
# Newton-Verfahren in Python                      Rev. 1.0 (16. Apr 2020)
# ===========================---------------------------------------------
# (C)opyleft in 2020 by N. Markgraf (nmarkgraf@hotmail.com)
#
# ========================================================================

from math import exp, fabs


def print_iter_info(i, x, fx, gx):
    print(f'Iter. {i}: x={x:.8F} f(x)={fx:.8F} g(x)={gx:.8F}')


def stefferson(f, x_start, max_iter=1000, epsilon=0.0001):
    x = x_start
    for i in range(1, max_iter):
        fx = f(x)
        if abs(fx) < epsilon:
            break
        gx = f(x+fx)/fx - 1  # =(f(x+fx))-fx/fx
        if abs(gx) < epsilon:
            break
        print_iter_info(i, x, fx, gx)
        x = x - (fx / gx)
    return x


def fkt(x):
    return -x**3+8*x**2-9*x-18


if __name__ == "__main__":
    print(f'Der x-Wert liegt bei {stefferson(fkt, 3.5):.10F} \n')
