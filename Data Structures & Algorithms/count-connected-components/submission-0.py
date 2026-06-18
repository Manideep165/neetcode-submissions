class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Initially, every node is its own parent.
        # Each node forms a separate connected component.
        par = [i for i in range(n)]

        # Rank stores the size of each component.
        rank = [1] * n

        def find(n1):

            # Start from the given node.
            res = n1

            # Keep moving upward until we reach the root.
            while res != par[res]:

                # Path compression:
                # Make nodes point closer to the root.
                par[res] = par[par[res]]

                res = par[res]

            # Return the root of the component.
            return res

        def union(n1, n2):

            # Find roots of both nodes.
            p1, p2 = find(n1), find(n2)

            # Already in the same component.
            if p1 == p2:
                return 0

            # Union by size/rank:
            # Attach the smaller tree under the larger tree.
            if rank[p2] > rank[p1]:

                par[p1] = p2

                # Update component size.
                rank[p2] += rank[p1]

            else:

                par[p2] = p1

                # Update component size.
                rank[p1] += rank[p2]

            # Successfully merged two components.
            return 1

        # Initially there are n separate components.
        res = n

        # Every successful union reduces the number
        # of connected components by 1.
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res