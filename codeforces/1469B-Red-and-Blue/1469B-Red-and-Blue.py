t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))

    m = int(input())
    b = list(map(int, input().split()))

    s = 0
    max_r = 0
    for x in r:
        s += x
        max_r = max(max_r, s)

    s = 0
    max_b = 0
    for x in b:
        s += x
        max_b = max(max_b, s)

    print(max_r + max_b)