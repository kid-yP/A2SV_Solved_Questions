"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
from typing import List

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def is_uniform(r: int, c: int, size: int) -> bool:
            """Check if all cells in grid[r:r+size][c:c+size] are the same."""
            val = grid[r][c]
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        return False
            return True

        def build(r: int, c: int, size: int) -> 'Node':
            if is_uniform(r, c, size):
                return Node(grid[r][c] == 1, True, None, None, None, None)
            half = size // 2
            topLeft = build(r, c, half)
            topRight = build(r, c + half, half)
            bottomLeft = build(r + half, c, half)
            bottomRight = build(r + half, c + half, half)
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(0, 0, n)