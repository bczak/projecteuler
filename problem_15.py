def fac(n):
    return 1 if n == 1 else n * fac(n - 1)


print(fac(40) / (fac(20) ** 2))
