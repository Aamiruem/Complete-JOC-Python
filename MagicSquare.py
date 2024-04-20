def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]

    num = 1
    i, j = 0, n // 2

    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        newi, newj = (i - 1) % n, (j + 1) % n
        if magic_square[newi][newj]:
            i += 1
        else:
            i, j = newi, newj

    return magic_square

# Example usage:
size = 3  # Size of the magic square (odd number)
magic_square = generate_magic_square(size)
for row in magic_square:
    print(row)
