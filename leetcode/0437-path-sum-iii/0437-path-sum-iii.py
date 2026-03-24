# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix_sum = {0: 1}
        return self.dfs(root, 0, targetSum, prefix_sum)

    def dfs(self, node, curr_sum, targetSum, prefix_sum):
        if not node:
            return 0

        curr_sum += node.val

        count = prefix_sum.get(curr_sum - targetSum, 0)

        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        count += self.dfs(node.left, curr_sum, targetSum, prefix_sum)
        count += self.dfs(node.right, curr_sum, targetSum, prefix_sum)

        prefix_sum[curr_sum] -= 1

        return count
