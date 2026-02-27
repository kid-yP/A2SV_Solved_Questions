from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = defaultdict(int)
window_count = 0
left = 0
tot_sum = 0

for right in range(n):
    if count[arr[right]] == 0:
        window_count += 1
    count[arr[right]] += 1

    while window_count > k:
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            window_count -= 1
        left += 1
    
    tot_sum += right - left + 1

print(tot_sum)
