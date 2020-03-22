# ========================================================================
# Uebung Doppelfolge                               rev. 1.0 (22.Mrz 2020)
# ==================------------------------------------------------------
# (C)opyleft in 2020 by N. Markgraf (nmarkgraf@hotmail.com)
#
# ========================================================================

from math import exp, fabs

def fkt(x, y):
    return 108.0-((815.0-1500.0/y) / x)


l = [4.0, 4.25]

for i in range(1, 100):
    l.append(fkt(l[i], l[i-1]))

print(l[80])
print(l[100])

print(l[10:30])