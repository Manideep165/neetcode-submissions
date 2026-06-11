"""
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val

        # List of neighboring nodes.
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Maps original nodes to their cloned copies.
        oldToNew = {}

        def dfs(node):

            # If this node was already cloned,
            # return the existing copy.
            if node in oldToNew:
                return oldToNew[node]

            # Create a clone of the current node.
            copy = Node(node.val)

            # Store the mapping before exploring neighbors.
            oldToNew[node] = copy

            # Clone all neighboring nodes.
            for nei in node.neighbors:

                # Add cloned neighbor to the copy.
                copy.neighbors.append(dfs(nei))

            # Return the cloned node.
            return copy

        # Handle empty graph.
        return dfs(node) if node else None