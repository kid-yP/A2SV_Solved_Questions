# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        freq = {}
        max_freq = 0

        def dfs(node):
            nonlocal max_freq
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            freq[total] = freq.get(total, 0) + 1
            max_freq = max(max_freq, freq[total])
            return total

        dfs(root)
        return [s for s, f in freq.items() if f == max_freq]