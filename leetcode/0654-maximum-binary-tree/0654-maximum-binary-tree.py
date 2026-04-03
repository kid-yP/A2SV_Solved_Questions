# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []

        for num in nums:
            curr = TreeNode(num)

            while stack and stack[-1].val < num:
                curr.left = stack.pop()

            if stack:
                stack[-1].right = curr
            
            stack.append(curr)
        
        return stack[0]