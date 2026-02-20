n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k == n:
    print(0)
else:
    total_cost = arr[-1] - arr[0]

    gaps = []
    for i in range(n - 1):
        gaps.append(arr[i + 1] - arr[i])
    
    gaps.sort(reverse = True)

    for i in range(k - 1):
        total_cost -= gaps[i]

    print(total_cost)
