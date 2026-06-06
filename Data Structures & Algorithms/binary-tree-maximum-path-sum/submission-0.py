# Definition for a binary tree node.
# Each node stores a value and references to left and right children.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Store the maximum path sum found so far.
        # A list is used so it can be modified inside dfs().
        res = [root.val]

        def dfs(root):

            # An empty node contributes 0 to a path.
            if not root:
                return 0

            # Recursively find the maximum path sum
            # coming from the left and right subtrees.
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # Ignore negative path sums because they
            # would only decrease the total path sum.
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            # Calculate the best path that passes
            # through the current node.
            #
            #        left
            #          \
            #           root
            #          /
            #       right
            #
            # This path may include:
            # root + left subtree + right subtree
            res[0] = max(
                res[0],
                root.val + leftMax + rightMax
            )

            # Return the maximum path that can be extended
            # to the parent.
            #
            # We can only choose ONE side because a parent
            # cannot continue through both branches.
            return root.val + max(leftMax, rightMax)

        # Start DFS traversal.
        dfs(root)

        # Return the overall maximum path sum.
        return res[0]