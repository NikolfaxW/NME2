import numpy as np
import sys
import math as m
import matplotlib.pyplot as plt

def print_hi(name):
    print(f'Hi, {name}')

def f(x):
    return float(16*x*x)

def df(x):
    result = float(32*x)
    return result

def dfvar1(x,h):
    result = float((f(x + h) - f(x))/h)
    return result

def dfvar2(x,h):
    result = float((f(x + h) - f(x - h))/(2*h))
    return result

def tenPrecentTest(initialValue, approximatedOne):
    return (abs(approximatedOne/initialValue) <= 0.90 or abs(approximatedOne/initialValue) >= 1.10 )

def Solve1():
    eps = sys.float_info.epsilon
    h = eps
    x = 1
    der_value = float(df(x))
    while(True):
        der_aprox_value = float(dfvar1(x,h))
        if(abs(der_aprox_value/der_value) <= 0.90 or abs(der_aprox_value/der_value) >= 1.10 ):
            break
        else:
            h = h * 2 #can be run with h = h + 2*eps in order to get more precise values, but require far more time.
    print("By multiplication we got that the step of first derivation approximation is : ", h)
    print("Approximated value is ", der_aprox_value)
    h1 = float(h/2)
    h2 = float(h)
    while(True):
        hdifference = float(h2 - h1)/2
        if(hdifference <= eps):
            if(h1 > h2):
                h = h1
            else:
                h = h2
            break
        nh = h1 + hdifference
        der_aprox_value = float(dfvar1(x, nh))
        if tenPrecentTest(der_value, der_aprox_value):
            h2 = nh
        else:
            h1 = nh
    print("By logarithmic contraction we got that the step of first derivation approximation is : ", h)
    print("Approximated value is ", der_aprox_value)

def getNextYn(yPrevios, n):
    return float((1/n) - (10*yPrevios))

def Solve2():
    N = 260

    ns = np.empty(N)
    ys = np.empty(N)
    ys[0] = m.log(11) - m.log10(10) # y0
    ns[0] = 0
    first = True
    for i in range(1,N):
        ys[i] = getNextYn(ys[i - 1], i)
        ns[i] = i
        if((ys[i] > 0 and ys[i - 1] < 0) or (ys[i] < 0 and ys[i - 1] > 0)) and first:
            print("It starts to oscilate? for n = ", i - 1)
            first = False



    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(ns, ys, label='y posloupnost', color='C1')
    ax.set_yscale('log')
    ax.set_xlabel('n')
    ax.set_ylabel('y_n')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    print("Solving the first part:")
    Solve1()

    print("Solving the second part:")
    Solve2()
