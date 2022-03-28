import numpy as np

def f(x):
    return x*np.exp(x+1)

def simspson(a, b, n, f):
    h = (b-a)/(2*n)
    #print(h)
    x_list = [a+i*h for i in range(n*2+1)]
    #print(x_list)
    f_list = [f(x) for x in x_list]
    #print(f_list)
    sum_2i = [f(x_list[2*i-1]) for i in range(1, n+1)]
    sum_n = [f(x_list[2*i]) for i in range(1, n)]
    res = h/3*(f(a)+4*sum(sum_2i)+2*sum(sum_n)+f_list[-1])
    return res

a = simspson(-1, 3, 25, f)
print(f"Результат интеграла: {a}")