# Definition for a binary tree node.
# Each node stores a value and references to left and right children.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Base case:
        # If either traversal list is empty,
        # there is no tree to construct.
        if not preorder or not inorder:
            return None

        # The first element in preorder traversal
        # is always the root of the current subtree.
        root = TreeNode(preorder[0])

        # Find the root's position in inorder traversal.
        # Everything to the left belongs to the left subtree.
        # Everything to the right belongs to the right subtree.
        mid = inorder.index(preorder[0])

        # Recursively build the left subtree.
        # preorder[1:mid+1] contains the left subtree nodes.
        # inorder[:mid] contains the left subtree nodes.
        root.left = self.buildTree(
            preorder[1:mid + 1],
            inorder[:mid]
        )

        # Recursively build the right subtree.
        # preorder[mid+1:] contains the right subtree nodes.
        # inorder[mid+1:] contains the right subtree nodes.
        root.right = self.buildTree(
            preorder[mid + 1:],
            inorder[mid + 1:]
        )

        # Return the constructed subtree root.
        return root