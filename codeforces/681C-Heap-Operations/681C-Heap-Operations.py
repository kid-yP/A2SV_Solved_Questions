import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []
result = []

for _ in range(n):
    parts = input().split()
    
    if parts[0] == "insert":
        x = int(parts[1])
        heapq.heappush(heap, x)
        result.append(f"insert {x}")
    
    elif parts[0] == "getMin":
        x = int(parts[1])
        
        while heap and heap[0] < x:
            heapq.heappop(heap)
            result.append("removeMin")
        
        if not heap or heap[0] > x:
            heapq.heappush(heap, x)
            result.append(f"insert {x}")
        
        result.append(f"getMin {x}")
    
    else:
        if not heap:
            heapq.heappush(heap, 0)
            result.append("insert 0")
        
        heapq.heappop(heap)
        result.append("removeMin")

print(len(result))
print("\n".join(result))