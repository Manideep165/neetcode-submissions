# Definition for a binary tree node.
# Each node stores a value and references to left and right children.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a binary tree into a string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        # Stores the serialized representation.
        res = []

        def dfs(node):

            # If the node is None, store a marker.
            if not node:
                res.append("N")
                return

            # Store the node's value.
            res.append(str(node.val))

            # Serialize the left subtree.
            dfs(node.left)

            # Serialize the right subtree.
            dfs(node.right)

        # Start preorder traversal.
        dfs(root)

        # Convert the list into a comma-separated string.
        return ",".join(res)

    # Decodes the string back into the original binary tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        # Split the serialized string into individual values.
        vals = data.split(",")

        # Pointer used to track the current position.
        self.i = 0

        def dfs():

            # If we encounter "N",
            # this represents a None node.
            if vals[self.i] == "N":
                self.i += 1
                return None

            # Create a new tree node using the current value.
            node = TreeNode(int(vals[self.i]))

            # Move to the next value.
            self.i += 1

            # Reconstruct the left subtree.
            node.left = dfs()

            # Reconstruct the right subtree.
            node.right = dfs()

            # Return the reconstructed node.
            return node

        # Start reconstruction from the root.
        return dfs()