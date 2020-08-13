from functools import reduce


def n_factors(n):
    return len(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def quad(n):
    return (n + 1) * n // 2


def main():
    f_min = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23
    print(n_factors(f_min))

    for i in range(32, 1000000):
        if n_factors(quad(i)) > 500:
            print(i, quad(i), n_factors(quad(i)))


if __name__ == '__main__':
    main()
