# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent=None, grandparent=None):
            if not node:
                return 0
            total = node.val if grandparent and grandparent.val % 2 == 0 else 0
            total += dfs(node.left, node, parent)
            total += dfs(node.right, node, parent)
            return total
        
        return dfs(root)
