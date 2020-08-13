res = 2
primes = [2]
for i in range(3, 2000000, 2):
    for p in primes:
        if i % p == 0:
            break
    else:
        primes.append(i)
        res += i
        print(i)

print(res)
