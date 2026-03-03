n, k, q = map(int, input().split())
temp = [0] * 200002
h = len(temp)

for _ in range(n):
    l, r = map(int, input().split())
    temp[l] += 1
    temp[r + 1] -= 1


for i in range(1, h):
    temp[i] = temp[i - 1] + temp[i]

for i in range(h):
    if temp[i] >= k:
        temp[i] = 1
    else: 
        temp[i] = 0 

for i in range(1, h):
    temp[i] = temp[i - 1] + temp[i]

for _ in range(q):
    a, b = map(int, input().split())
    print(temp[b] - temp[a - 1])
