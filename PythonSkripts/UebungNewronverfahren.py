# ========================================================================
# Uebung Newtonverfahren in Python                 rev. 1.0 (22.Mrz 2020)
# =================================---------------------------------------
# (C)opyleft in 2020 by N. Markgraf (nmarkgraf@hotmail.com)
#
# ========================================================================

import matplotlib.pyplot as plt
import numpy as np

# Betrachteter Bereich 0 - 10,5
x = np.arange(0, 10.5, 0.1)

# Gewinnfunktion G(x) = P(x)*x - K(X)
y = (100-x)*x - (2*x**3-25*x**2+134*x+60)

# Bereich plotten
plt.plot(x, y)

# X-Achse benennen
plt.xlabel('Menge [x]')

# Y-Achse benennen
plt.ylabel('Gewinn [y=G(x)]')

# Titel fuer den Graphen:
plt.title('Gewinnfunktion')

# Gitterraster zeichnen
plt.grid(True)

# Fette X-Achse in schwarz
plt.axhline(0, color='black', lw=2)

# Nullstellen der Funktion mit roten Punkten markieren
plt.plot([3, 10], [0, 0], 'ro')

# Bemerkung welcher Punkt (hier Break Even Point) gesucht ist
plt.annotate('Break Even point', xy=(3, 0.01), xytext=(0, 50),
             arrowprops=dict(facecolor='green', shrink=0.08),
             )

# Graphik anzeigen
plt.show()
