t=int(input())

for _ in range(t):
    n,coins=map(int,input().split())
    casinos=[tuple(map(int,input().split())) for _ in range(n)]
    
    casinos.sort()
    used=[0]*n

    changed=True
    while changed:
        changed=False

        for i in range(n):
            l,r,real=casinos[i]

            if not used[i] and l<=coins<=r and real>coins:
                coins=real
                used[i]=1
                changed=True

    print(coins)
