# Definition for a binary tree node.
# Each node stores a value and references to left and right children.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Helper function that checks whether a subtree is a valid BST.
        # 'left' and 'right' define the valid range for node values.
        def valid(node, left, right):

            # An empty subtree is always a valid BST.
            if not node:
                return True

            # The current node's value must lie strictly between
            # the allowed lower and upper bounds.
            if not (node.val < right and node.val > left):
                return False

            # Recursively validate:
            # - Left subtree: values must be < current node's value.
            # - Right subtree: values must be > current node's value.
            return (
                valid(node.left, left, node.val) and
                valid(node.right, node.val, right)
            )

        # Start with the widest possible range:
        # (-∞, +∞)
        return valid(root, float("-inf"), float("inf"))