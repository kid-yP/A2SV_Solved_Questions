from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = defaultdict(int)
window_count = 0
l = 0
long_l, long_r = 0, 0

for r in range(n):
    if freq[arr[r]] == 0:
        window_count += 1
    freq[arr[r]] += 1

    while window_count > k:
        freq[arr[l]] -= 1
        if freq[arr[l]] == 0:
            window_count -= 1
        l += 1
    if r - l > long_r - long_l:
        long_l = l
        long_r = r

print(long_l + 1, long_r + 1)
