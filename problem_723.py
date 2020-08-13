from math import sqrt


def get_lattice_grid_points(r):
    points = []

    for a in range(int(r)):
        b = sqrt(r * r - a * a)
        b_int = int(b)
        if b == b_int:
            points.append((a, b_int))
    return points


def f(r):
    points = get_lattice_grid_points(r)
    print(points)


if __name__ == '__main__':
    f(sqrt(1411033124176203125 / 5))
