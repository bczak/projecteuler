from math import comb


def compute_colors_proba(balls, select_colors, all_colors):
    probability = comb(all_colors, select_colors)

    for i in range(20):
        probability *= (select_colors * 10 - i) / (balls - i)

    result = probability

    for i in range(2, select_colors):
        result -= probability * compute_colors_proba(select_colors * 10, i, select_colors)

    return result


def main():
    res = 0
    for i in range(1, 8):
        proba = compute_colors_proba(70, i, 7)
        res += i * proba
        print(i, proba)

    print()
    print(f'{res:.11}')


if __name__ == '__main__':
    main()
