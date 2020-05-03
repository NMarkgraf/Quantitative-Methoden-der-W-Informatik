# ========================================================================
# Newton-Verfahren Polynominterpolation in Python  Rev. 1.0 (03. Mai 2020)
# =================================---------------------------------------
# (C)opyleft in 2020 by N. Markgraf (nmarkgraf@hotmail.com)
#
# ========================================================================
import numpy as np

def divdiff(x, y):
    n = len(y)
    T = [[0] * (n-i) for i in range(n)]
    for i in range(n):
        T[i][0] = y[n-i-1]
    for level in range(1, n):
        for i in range(n - level):
            T[i][level] = (T[i+1][level-1] - T[i][level-1]) / (x[n-(i+level)-1]-x[n-i-1])
    return T


def newton_koeffizenten(divdif, n):
    ret = [divdif[n - i - 1][i] for i in range(n)]
    return ret


def newtonpolyeval(r, x, koeff):
    n = len(koeff) - 1
    temp = koeff[n]
    for i in range(n-1, -1, -1):
        temp = temp * (r - x[i]) + koeff[i]
    return temp

if __name__ == "__main__":
    x = [-1,0,1]
    y = [12, 7, 4]

    divdif = divdiff(x, y)
    print(f'Dividierte Differenzen:{divdif}')

    koeff = newton_koeffizenten(divdif, len(x))
    print(f'Newton-Koeffizenten: {koeff}')

    print(f'f(-2)={newtonpolyeval(-2, x, koeff)}')
