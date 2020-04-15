# ========================================================================
# Sekantenverfahren in Python                      Rev. 2.0 (13. Apr 2020)
# ===========================---------------------------------------------
# (C)opyleft in 2020 by N. Markgraf (nmarkgraf@hotmail.com)
#
# ========================================================================

from math import exp, fabs


def print_iter_info(i, x, fx, dfx):
    print(f'Iter. {i}: x={x:.8F} f(x)={fx:.8F} \u0394f(x)={dfx:.8F}')


def sekantenverfahren(f, x_0, x_1, max_iter=1000, epsilon=0.0001):
    x_last, x_cur, fx = x_0, x_1, f(x_last)
    for i in range(1, max_iter):
        fxl, fx = fx, f(x_cur)
        dfx = (fxl - fx) / (x_last - x_cur)
        print_iter_info(i, x_cur, fx, dfx)
        if abs(fx) < epsilon: 
            break
        x_last, x_cur = x_cur, x_last - (fx / dfx)
    return x_cur


def fkt(x):
    return -x**3+8*x**2-9*x-18


if __name__ == "__main__":
    print('Der x-Wert liegt bei '
          f'{sekantenverfahren(fkt, 2, 4, epsilon=0.0000001):.10F}\n')
