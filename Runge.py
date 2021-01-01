import matplotlib.pyplot as plt
import math

def func( x, y ):
    return (y-x**2+1);

a = []
b = []

def RungeKutta(x0, y0, x, h):

    n = (int)((x-x0)/h)
    y = y0
    i =1
    while(i< n+1):
        print(y)
        a.append(x0)
        b.append(y)
        k1 = h * func(x0, y)
        k2 = h * func(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * func(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * func(x0 + h, y + k3)

        # Update next value of y
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

        # Update next value of x
        x0 = x0 + h
        i = i+1
    return y


x0 = 0
y = 0.5
x = 10
h = 0.1
print (RungeKutta(x0, y, x, h))
plt.plot(a,b)
plt.show()
