n = int(input())
a = list(map(int, input().split()))

a.sort()
days = 0

for problems in a:
    if problems >= days + 1:
        days += 1

print(days)
