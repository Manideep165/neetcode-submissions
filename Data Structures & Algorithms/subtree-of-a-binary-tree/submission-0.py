# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # An empty tree is always a subtree.
        if not subRoot:
            return True

        # If the main tree is empty but subRoot isn't,
        # subRoot cannot be found.
        if not root:
            return False

        # Check if the subtree rooted at the current node
        # is identical to subRoot.
        if self.sameTree(root, subRoot):
            return True

        # Otherwise, recursively search in the left and right
        # subtrees of the current node.
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def sameTree(self, root, subRoot):

        # If both nodes are None, the trees match here.
        if not root and not subRoot:
            return True

        # If both nodes exist and their values are equal,
        # recursively compare their left and right children.
        if root and subRoot and root.val == subRoot.val:
            return (
                self.sameTree(root.left, subRoot.left) and
                self.sameTree(root.right, subRoot.right)
            )

        # Trees do not match.
        return False