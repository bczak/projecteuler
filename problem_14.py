def get_chain(n):
    s = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        s += 1
    return s


best = [0, 0]
for i in range(1, 1000000):
    chain = get_chain(i)
    print(i)
    if best[1] < chain:
        best[0] = i
        best[1] = chain

print(best)
