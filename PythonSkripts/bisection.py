# ========================================================================
# Bisection-Verfahren in Python                    rev. 1.0 (22.Mrz 2020)
# =============================-------------------------------------------
# (C)opyleft in 2020 by N. Markgraf (nmarkgraf@hotmail.com)
#
# ========================================================================

from math import exp, fabs


def print_iter_info(i, a, b, c, f):
    print('Iter. %i: a=%2.8F fkt(a)=%2.8F c=(a+b)/2=%2.8F fkt(c)= %2.8F' %
          (i, a, f(a), c, f(b)) +
          ' b=%2.8F  fkt(b)=%2.8F\n' % (b, f(b)))


def bisection(f, a, b, maxitr=1000, minwidth=1.0/1000):
    if f(a) * f(b) > 0:
        raise ArithmeticError("Das Produkt der Intervallgrenzen muss " +
                              "ein Vorzeichenwechsel haben!")
    if a > b:
        a, b = b, a
    iw = b - a
    i = 1
    while iw > minwidth:
        c = (a+b)/2.0
        print_iter_info(i, a, b, c, f)
        i = i + 1
        if i > maxitr:
            break
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
    print('Der x-Wert liegt zwischen %2.8F und %2.8F \n' %
          (intervall_links, intervall_rechts))
