# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode | None) -> list[list[str]]:
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        h = depth(root)
        rows = h
        cols = 2 ** h - 1
        res = [[""] * cols for _ in range(rows)]

        def fill(node, r, c):
            if not node:
                return
            res[r][c] = str(node.val)
            if r + 1 < rows:
                offset = 2 ** (h - r - 2)
                fill(node.left, r + 1, c - offset)
                fill(node.right, r + 1, c + offset)

        fill(root, 0, (cols - 1) // 2)
        return res