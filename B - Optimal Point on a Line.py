n = int(input())
coor = list(map(int, input().split()))

coor.sort()

if n % 2 == 1: 
    print(coor[n // 2]) 
else: 
    print(coor[n // 2 - 1])
