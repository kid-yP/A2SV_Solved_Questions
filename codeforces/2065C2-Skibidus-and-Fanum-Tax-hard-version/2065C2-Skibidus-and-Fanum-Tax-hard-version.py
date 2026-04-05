import bisect

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    b.sort()
    
    prev = -10**18
    ok = True
    
    for x in a:
        best = float('inf')
        
        if x >= prev:
            best = x
        
        target = prev + x
        idx = bisect.bisect_left(b, target)
        
        if idx < m:
            val = b[idx] - x
            if val >= prev:
                best = min(best, val)
        
        if best == float('inf'):
            ok = False
            break
        
        prev = best
    
    print("YES" if ok else "NO")