# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def invertTree(
        self,
        root: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        # Base case
        #
        # If node does not exist,
        # nothing to invert
        if not root:
            return None

        # Store left child temporarily
        tmp = root.left

        # Swap children
        #
        # left becomes right
        root.left = root.right

        # right becomes old left
        root.right = tmp

        # Recursively invert left subtree
        self.invertTree(root.left)

        # Recursively invert right subtree
        self.invertTree(root.right)

        # Return root of inverted tree
        return root