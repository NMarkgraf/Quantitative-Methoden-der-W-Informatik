from math import exp

def print_iter_info(x):
    #x.sort()
    print(f'a={x[0]} b={x[1]} c={x[2]}')

def mueller(f, a, b, r, max_iter=1000, epsilon=0.0001):
    x = [a, b, r]
    root = r
    print_iter_info(x)
    for i in range(1, max_iter):
        x.sort()
        x = [x[1], x[2], x[0]]
        y = list(map(f, x))
        h1 = x[1] - x[0]
        h2 = x[0] - x[2]
        # print(f'{h1} {h2}')
        if abs(h1) < epsilon:
            break
        if abs(h2) < epsilon:
            break
        lam = h2 / h1
        c = y[0]
        a = (lam * y[1] - y[0] * ((1.0 + lam)) + y[2]) / (lam * h1 ** 2.0 * (1 + lam))
        b = (y[1] - y[0] - a * ((h1) ** 2.0)) / (h1)
        if b > 0:
            root = x[0] - ((2.0 * c) / (b + (b ** 2 - 4.0 * a * c) ** 0.5))
        else:
            root = x[0] - ((2.0 * c) / (b - (b ** 2 - 4.0 * a * c) ** 0.5))

        if abs(f(root)) < epsilon:
            break

        if abs(f(root)) > x[0]:
            x = [x[1], x[0], root]
        else:
            x = [x[2], x[0], root]
        print_iter_info(x)
    return(root)


def fktA(x):
    return (exp(-x ** 2) - x)

def fktB(x):
    return -1.5*x**2+12*x-18
    
if __name__ == "__main__":
    print(mueller(fktB, 1.0, 2.5, 3.0))  # , epsilon=0.0000001))  # 0, 1, 0.5, epsilon=0.000001))
    print(mueller(fktA, 0.2, 1.5, 0.5, epsilon=0.0000001))  # 0, 1, 0.5, epsilon=0.000001))
