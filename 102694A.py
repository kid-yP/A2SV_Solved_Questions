import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    graph[u].append(v)
    graph[v].append(u)


def dfs(node):
    stack = [(node, -1, 0)]
    res = [0, node]

    while stack:
        v, p, d = stack.pop()
        if d > res[0]:
            res[0] = d
            res[1] = v

        for ne in graph[v]:
            if ne != p:
                stack.append((ne, v, d + 1))

    return res


print(3 * dfs(dfs(0)[1])[0])
