# ========================================================================
# Newton-Fourier-Verfahren in Python              Rev. 1.0 (13. Apr 2020)
# ==================================--------------------------------------
# (C)opyleft in 2020 by N. Markgraf (nmarkgraf@hotmail.com)
#
# ========================================================================

from math import exp, fabs


def print_iter_info(i, x, z, fx, fz, dfx):
    print(f'Iter. {i}: x={x:.8F} z={z:.8F} f(x)={fx:.8F} f(z)={fz:.8F} f\'(x)={dfx:.8F}')


def newtonfourier(f, df, x_start, z_start, max_iter=1000, epsilon=0.0001):
    x, z = x_start, z_start
    if f(x) * f(z) > 0:
        raise ArithmeticError("Das Produkt der Intervallgrenzen muss "
                              "ein Vorzeichenwechsel haben!")
    if df(x) * df(z) <= 0:
        raise ArithmeticError("Das Produkt der Steigung in den Intervallgrenzen " 
                              "darf kein Vorzeichenwechsel haben!")
    if x > z:
        x, z = z, x
    for i in range(1, max_iter):
        fx, fz, dfx = f(x), f(z), df(x)
        print_iter_info(i, x, z, fx, fz, dfx)
        if dfx*df(z) <= 0:
            raise ArithmeticError("Das Produkt der Steigung in den Intervallgrenzen "
                                  "darf kein Vorzeichenwechsel haben!")
        if abs(fx) < epsilon or abs(dfx) < epsilon:
            break
        x, z = (x - (fx / dfx)), (z - (fz / dfx))
    return x, z


def fkt(x):
    return -x**3+8*x**2-9*x-18


def dfkt(x):
    return -3*x**2+16*x-9


if __name__ == "__main__":
    a, b = newtonfourier(fkt, dfkt, 1.21, 4,epsilon=0.0000001)
    print(f'Der x-Wert liegt zwischen {a:.10F} und {b:.10F} \n')
