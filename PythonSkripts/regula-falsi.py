# ========================================================================
# Regular-Falsi-Verfahren in Python               Rev. 1.0 (15. Apr 2020)
# =================================---------------------------------------
# (C)opyleft in 2020 by N. Markgraf (nmarkgraf@hotmail.com)
#
# ========================================================================

from math import exp


def print_iter_info(i, a, b, c, f):
    print(f'Iter. {i}: a={a:.8F} f(a)={f(a):.8F} c={c:2.8F} '
          f'f(c)={f(c):.8F} b={b:.8F}  f(b)={f(b):.8F}')

          
def regularfalsi(f, a, b, max_iter=1000, epsilon=0.0001):
    if f(a) * f(b) > 0:
        raise ArithmeticError("Das Produkt der Intervallgrenzen muss " +
                              "ein Vorzeichenwechsel haben!")
    if a > b:
        a, b = b, a
    fa, fb = f(a), f(b)
    for i in range(1, max_iter):
        iw = b - a
        if iw < epsilon:
            break
        c = a - (iw / (fb - fa)) * fa
        fc = f(c)
        print_iter_info(i, a, b, c, f)
        if fb*fc <= 0:
            a, fa = c, fc
        else:
            b, fb = c, fc
    return a, b


def fkt(x):
    return -x**3+8*x**2-9*x-18


if __name__ == "__main__":
    intervall_links, intervall_rechts = regularfalsi(fkt, 2, 4)
    print(f'Der x-Wert liegt zwischen {intervall_links:.10F} '
          f'und {intervall_rechts:.10F}')

