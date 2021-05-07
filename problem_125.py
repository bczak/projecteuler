def is_poly(n):
    return str(n) == str(n)[::-1]


palindromes = set()
for i in range(1, 10000):
    j = i + 1
    total_tmp = j * j + i * i
    j += 1
    while total_tmp < 10 ** 8:
        if is_poly(total_tmp):
            palindromes.add(total_tmp)
        total_tmp += j * j
        j += 1

print(sum(palindromes))
