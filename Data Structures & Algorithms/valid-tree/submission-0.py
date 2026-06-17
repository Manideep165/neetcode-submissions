class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Edge case: empty graph.
        if not n:
            return True

        # Build adjacency list.
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:

            # Undirected graph:
            # add both directions.
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Tracks visited nodes.
        visit = set()

        def dfs(i, prev):

            # If we've already visited this node,
            # a cycle exists.
            if i in visit:
                return False

            # Mark node as visited.
            visit.add(i)

            # Explore neighbors.
            for j in adj[i]:

                # Ignore the node we came from.
                if j == prev:
                    continue

                # If a cycle is found below,
                # the graph is not a tree.
                if not dfs(j, i):
                    return False

            return True

        # Conditions for a valid tree:
        # 1. No cycles
        # 2. All nodes connected
        return dfs(0, -1) and len(visit) == n