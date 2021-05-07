def count_rects(a, b):
    if a == b == 1:
        return 1
    res = 1
    if a > 1:
        res += count_rects(a - 1, b) * 2
    if b > 1:
        res += count_rects(a, b - 1) * 2
    if a >= 1 and b >= 1:
        res -= count_rects(a - 1, b - 1)
    return res


print(count_rects(2, 2))
