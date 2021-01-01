
def l():
    x = 1
    i = 1
    x_b = 0
    while (abs(x-x_b>0.00001)):
        x_b = x
        x = f(x)
        print(i, "{0:.6f}".format(x),"{0:.6f}".format(abs(x-x_b)))
        i=i+1


def e(n):
    e=0.0
    for i in range(0,n+1):
        e = e+(1/factorial(i))
    return e

def f(x):
    return (2*(x)**2 + 5)**(1/3)


l()
