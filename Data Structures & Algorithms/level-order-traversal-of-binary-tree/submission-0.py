# Definition for a binary tree node.
# Each node stores a value and references to left and right children.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Stores the final level-order traversal result.
        # Each inner list contains values from one level.
        res = []

        # Create a queue for Breadth-First Search (BFS).
        q = collections.deque()

        # Start by adding the root node to the queue.
        q.append(root)

        # Continue while there are nodes left to process.
        while q:

            # Number of nodes currently in the queue.
            # These all belong to the same level.
            qlen = len(q)

            # Stores values for the current level.
            level = []

            # Process exactly qlen nodes (one level).
            for i in range(qlen):

                # Remove the front node from the queue.
                node = q.popleft()

                # Ignore None nodes.
                if node:

                    # Add the node's value to the current level.
                    level.append(node.val)

                    # Add the left child to the queue.
                    q.append(node.left)

                    # Add the right child to the queue.
                    q.append(node.right)

            # If the level contains values, add it to the result.
            if level:
                res.append(level)

        # Return the level-order traversal.
        return res