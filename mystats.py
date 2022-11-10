def myavg(lst):
    t = 0
    n = 0
    for i in lst:
        t += i
        n += 1
    return t/n

def residual(lst1,lst2):
    n = len(lst1)
    s = 0
    for i in range(n):
        d = (lst1[i] - lst2[i])
        s += d
    return s

def residualsq(lst1,lst2):
    n = len(lst1)
    s = 0
    for i in range(n):
        d = (lst1[i] - lst2[i]) ** 2
        s += d
        print(i, lst1[i], lst2[i], d, s)
    return s

def meanDif(lst):
    t = 0
    avg = myavg(lst)
    for x in lst:
        t += (x - avg) ** 2
    return t


