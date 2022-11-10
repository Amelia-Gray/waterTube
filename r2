def residual(lst1,lst2):
    n = len(lst1)
    s = 0
    for i in range(n):
        print(i, lst1[i], lst2[i])
        d = (lst1[i] - lst2[i]) ** 2
        s += d
    return s
