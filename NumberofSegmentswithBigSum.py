n, s = map(int, input().split())
arr = list(map(int, input().split()))

window_sum = 0
left = 0
count = 0

for right in range(n):
    window_sum += arr[right]
    
    while window_sum >= s:
        count += n - right
        window_sum -= arr[left]
        left += 1

print(count)
