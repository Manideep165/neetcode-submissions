# Definition for a binary tree node.
# Each node contains a value and references to left and right children.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val      # Store the node's value
#         self.left = left    # Reference to the left child
#         self.right = right  # Reference to the right child

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # If both nodes are None, the trees match at this position.
        if not p and not q:
            return True

        # Return False if:
        # 1. One node exists and the other doesn't, or
        # 2. The values of the nodes are different.
        if not p or not q or p.val != q.val:
            return False

        # Recursively compare:
        # - the left subtrees of both nodes
        # - the right subtrees of both nodes
        # Both comparisons must be True for the trees to be identical.
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))