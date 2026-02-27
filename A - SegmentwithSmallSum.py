n, s = map(int, input().split())
arr = list(map(int, input().split()))

small_sum = 0
curr_sum = 0

left = 0
for right in range(n):
    curr_sum += arr[right]
    while curr_sum > s:
        curr_sum -= arr[left]
        left += 1
    small_sum = max(small_sum, right - left + 1)

print(small_sum)
