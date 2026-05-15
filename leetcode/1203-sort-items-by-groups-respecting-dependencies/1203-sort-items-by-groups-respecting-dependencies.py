class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
    
        item_graph = defaultdict(list)
        item_indegree = [0] * n
        group_graph = defaultdict(list)
        group_indegree = [0] * m
        
        for v in range(n):
            for u in beforeItems[v]:
                item_graph[u].append(v)
                item_indegree[v] += 1
                if group[u] != group[v]:
                    group_graph[group[u]].append(group[v])
                    group_indegree[group[v]] += 1
        
        def topo_sort(graph, indegree, nodes):
            q = deque([i for i in nodes if indegree[i] == 0])
            order = []
            while q:
                u = q.popleft()
                order.append(u)
                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
            return order if len(order) == len(nodes) else []
        
        group_order = topo_sort(group_graph, group_indegree, list(range(m)))
        if not group_order:
            return []
        
        item_order = topo_sort(item_graph, item_indegree, list(range(n)))
        if not item_order:
            return []
        
        items_in_group = defaultdict(list)
        for item in item_order:
            items_in_group[group[item]].append(item)
        
        result = []
        for g in group_order:
            result.extend(items_in_group[g])
        
        return result