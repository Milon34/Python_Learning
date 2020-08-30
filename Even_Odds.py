n, k = [int(i) for i in input().split()]


if n % 2 == 0:
    if k <= n / 2:
        m = 2 * k - 1
    else:
        m = 2 * (k - n // 2)
else:
    if k <= (n + 1) / 2:
        m = 2 * k - 1
    else:
        m = 2 * (k - (n + 1) // 2)
print(m)
a=[n]