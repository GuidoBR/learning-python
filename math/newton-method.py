# http://danielhomola.com/2016/02/09/newtons-method-with-10-lines-of-python/

def dx(f, x):
    return abs(0-f(x))


def newtons_method(f, df, x0, e):
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0)/df(x0)
        delta = dx(f, x0)
    print("Root is at {}".format(x0))
    print("f(x) at root is {} ".format(f(x0)))


def f(x):
    return 6*x**5-5*x**4-4*x**3+3*x**2

def df(x):
    return 30*x**4-20*x**3-12*x**2+6*x


if __name__ == "__main__":
    x0s = [0, .5, 1]
    for x0 in x0s:
        newtons_method(f, df, x0, 1e-5)
