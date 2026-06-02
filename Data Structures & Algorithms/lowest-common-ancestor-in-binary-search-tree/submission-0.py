# Definition for a binary tree node.
# Each node stores a value and references to left and right children.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Start traversing from the root of the BST.
        cur = root

        # Continue until the Lowest Common Ancestor is found.
        while cur:

            # If both p and q have values greater than the current node,
            # then both nodes must be in the right subtree.
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right

            # If both p and q have values smaller than the current node,
            # then both nodes must be in the left subtree.
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left

            # Otherwise, p and q are on different sides of the current node
            # (or one of them is the current node itself).
            # Therefore, the current node is their Lowest Common Ancestor.
            else:
                return cur