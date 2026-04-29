"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {emp.id: emp for emp in employees}
        total = 0
        queue = deque([id])
        
        while queue:
            emp_id = queue.popleft()
            emp = emp_map[emp_id]
            total += emp.importance
            queue.extend(emp.subordinates)
        
        return total