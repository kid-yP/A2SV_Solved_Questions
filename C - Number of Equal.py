n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, 0
ans = 0

while i < n and j < m:
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        val = a[i]
        
        count_a = 0
        while i < n and a[i] == val:
            count_a += 1
            i += 1
        
        count_b = 0
        while j < m and b[j] == val:
            count_b += 1
            j += 1
        
        ans += count_a * count_b

print(ans)
