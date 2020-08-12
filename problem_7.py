#!/usr/bin/python3

# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

primes = []

i = 2

while(len(primes) != 10001):
    is_not_prime = False
    for k in range(2, i):
        if i % k == 0 and i != k:
            is_not_prime = True
            break
    if is_not_prime: 
        i+=1
        continue
    primes.append(i)
    i += 1

print(primes[10000])