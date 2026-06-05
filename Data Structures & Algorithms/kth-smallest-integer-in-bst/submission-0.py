# Definition for a binary tree node.
# Each node stores a value and references to left and right children.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Counter to track how many nodes have been visited.
        n = 0

        # Stack used for iterative inorder traversal.
        stack = []

        # Start traversal from the root.
        cur = root

        # Continue while there are nodes to process
        # either in the tree or in the stack.
        while cur or stack:

            # Traverse as far left as possible,
            # pushing each node onto the stack.
            while cur:
                stack.append(cur)
                cur = cur.left

            # Pop the leftmost unvisited node.
            cur = stack.pop()

            # Visit the node.
            n += 1

            # If this is the kth visited node,
            # return its value.
            if n == k:
                return cur.val

            # Move to the right subtree.
            cur = cur.right
