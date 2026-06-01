# Definition for a binary tree node.
# This class represents each node in the binary tree.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val      # Store the node's value
#         self.left = left    # Reference to the left child
#         self.right = right  # Reference to the right child

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case:
        # If the current node is None (empty tree/subtree),
        # its depth is 0.
        if not root:
            return 0

        # Recursively find the depth of the left subtree
        # and the depth of the right subtree.
        # Take the larger of the two depths and add 1
        # to count the current node.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))