t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = [
        "aa",
        "aba",
        "aca",
        "abca",
        "acba",
        "accabba",
        "abbacca"
    ]
    for a in ans:
        if a in s:
            print(len(a))
            break
    else:
        print(-1)
