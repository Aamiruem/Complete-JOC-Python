def josephus(n, k):
    if n == 1:  # Base case: If there is only one soldier, that soldier survives
        return 1
    else:
        # Recursively calculate the position of the survivor after eliminating k-th soldier
        return (josephus(n - 1, k) + k - 1) % n + 1

# Number of soldiers and elimination factor
n = 25
k = 3

# Calculate the position of the survivor
result = josephus(n, k)

# Print the position of the survivor
print(result)
