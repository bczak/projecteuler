from functools import lru_cache


@lru_cache
def count(size, tiles, tile_size):
    if tile_size * tiles > size:
        return 0
    if tile_size * tiles == size:
        return 1
    if tiles == 1:
        return size - tile_size + 1

    total = 0
    for i in range(tile_size, size - (tiles - 1) * tile_size + 1):
        total += count(size - i, tiles - 1, tile_size)

    return total


def count_for_tile(size, tile_size):
    total = 0
    for i in range(1, (size // tile_size) + 1):
        total += count(size, i, tile_size)
    return total


print(count_for_tile(50, 2), count_for_tile(50, 3), count_for_tile(50, 4))
print(count_for_tile(50, 2) + count_for_tile(50, 3) + count_for_tile(50, 4))
