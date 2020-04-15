# ========================================================================
# Bisection-Verfahren in Python                  Rev. 2.0 (13. Apr. 2020)
# =============================-------------------------------------------
# (C)opyleft in 2020 by N. Markgraf (nmarkgraf@hotmail.com)
#
# ========================================================================

from math import exp, fabs


def print_iter_info(i, a, b, c, f):
    print(f'Iter. {i}: a={a:.8F} f(a)={f(a):.8F} c=(a+b)/2={c:.8F} '
          f'f(c)={f(c):.8F} b={b:.8F} f(b)={f(b):.8F}')


def bisection(f, a, b, max_iter=1000, epsilon=0.0001):
    if f(a) * f(b) > 0:
        raise ArithmeticError("Das Produkt der Intervallgrenzen muss "
                              "ein Vorzeichenwechsel haben!")
    if a > b:
        a, b = b, a
    iw = b - a
    for i in range(1, max_iter):
        if iw < epsilon:
            break
        c = (a+b)/2.0
        print_iter_info(i, a, b, c, f)
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c
        iw = b - a
    return a, b


def fkt(x):
    return exp(-x**2)-x


if __name__ == "__main__":
    intervall_links, intervall_rechts = bisection(fkt, 0, 1)
    print(f'Der x-Wert liegt zwischen {intervall_links:.10F} '
          f'und {intervall_rechts:.10F}')
