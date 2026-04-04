import bisect

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    b.sort()
    
    prev = -10**18
    
    possible = True
    
    for i in range(n):
        keep = a[i]
        
        target = prev + a[i]
        idx = bisect.bisect_left(b, target)
        
        change = float('inf')
        if idx < m:
            change = b[idx] - a[i]
        
        best = float('inf')
        
        if keep >= prev:
            best = min(best, keep)
        
        if change >= prev:
            best = min(best, change)
        
        if best == float('inf'):
            possible = False
            break
        
        prev = best
    
    print("YES" if possible else "NO")