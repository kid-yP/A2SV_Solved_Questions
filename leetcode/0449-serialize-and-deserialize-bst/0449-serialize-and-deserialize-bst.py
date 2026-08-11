# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string (preorder traversal)."""
        if not root:
            return ""
        # Recursive preorder
        def dfs(node):
            if not node:
                return []
            return [str(node.val)] + dfs(node.left) + dfs(node.right)
        return " ".join(dfs(root))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        vals = list(map(int, data.split()))
        self.idx = 0   # pointer to current position in vals

        def build(min_val: int, max_val: int) -> Optional[TreeNode]:
            if self.idx >= len(vals):
                return None
            val = vals[self.idx]
            # Check if this value can be placed in the current subtree
            if val < min_val or val > max_val:
                return None
            self.idx += 1
            node = TreeNode(val)
            # Left subtree: values must be < val
            node.left = build(min_val, val)
            # Right subtree: values must be > val
            node.right = build(val, max_val)
            return node

        return build(float('-inf'), float('inf'))