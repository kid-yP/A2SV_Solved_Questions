class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        queue = deque([i for i in range(n) if indegree[i] == 0])
        
        ancestors = [set() for _ in range(n)]
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                ancestors[v].add(u)
                ancestors[v].update(ancestors[u])
                
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        return [sorted(list(ans)) for ans in ancestors]
