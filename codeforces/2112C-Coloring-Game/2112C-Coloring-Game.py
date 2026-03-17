t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    ans = 0
    
    for k in range(2, n):
        limit = max(arr[k], arr[n-1] - arr[k])
        
        i = 0
        j = k - 1
        
        while i < j:
            if arr[i] + arr[j] > limit:
                ans += (j - i)
                j -= 1
            else:
                i += 1
    
    print(ans)