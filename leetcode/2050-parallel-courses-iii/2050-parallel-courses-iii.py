class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        finish = [0] * n
        
        for u, v in relations:
            graph[u-1].append(v-1)
            indegree[v-1] += 1
        
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                finish[i] = time[i]
                q.append(i)
        
        while q:
            u = q.popleft()
            for v in graph[u]:
                finish[v] = max(finish[v], finish[u] + time[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        return max(finish)