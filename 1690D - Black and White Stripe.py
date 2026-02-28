t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cards = input().strip()

    whites = 0
    ans = float('inf')
    left = 0

    for right in range(n):
        if cards[right] == 'W':
            whites += 1
        
        if right - left + 1 > k:
            if cards[left] == 'W':
                whites-= 1
            left += 1

        if right - left + 1 == k:
            ans = min(ans, whites)

    print(ans)
