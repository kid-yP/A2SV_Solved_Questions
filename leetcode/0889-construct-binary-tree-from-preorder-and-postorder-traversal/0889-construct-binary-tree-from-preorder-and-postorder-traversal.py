# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        j = 0 # index for postorder

        for val in preorder[1:]:
            node = TreeNode(val)

            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)

            while stack and stack[-1].val == postorder[j]:
                stack.pop()
                j += 1

        return root