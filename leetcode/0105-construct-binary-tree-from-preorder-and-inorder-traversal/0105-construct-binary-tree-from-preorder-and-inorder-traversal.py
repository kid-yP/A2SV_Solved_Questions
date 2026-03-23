# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        self.pre_idx = 0
        
        def array_to_tree(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            root.left = array_to_tree(left, inorder_map[root_val] - 1)
            root.right = array_to_tree(inorder_map[root_val] + 1, right)
            
            return root
        
        return array_to_tree(0, len(inorder) - 1)
