class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Edge case: empty grid.
        if not grid:
            return 0

        # Get dimensions of the grid.
        rows, cols = len(grid), len(grid[0])

        # Stores cells that have already been visited.
        visit = set()

        # Counts the number of islands found.
        islands = 0

        def bfs(r, c):

            # Queue for Breadth-First Search.
            q = collections.deque()

            # Mark starting cell as visited.
            visit.add((r, c))

            # Add starting cell to queue.
            q.append((r, c))

            while q:

                # Remove the front cell.
                row, col = q.popleft()

                # Four possible directions:
                # down, up, right, left
                directions = [
                    [1, 0],
                    [-1, 0],
                    [0, 1],
                    [0, -1]
                ]

                for dr, dc in directions:

                    # Calculate neighboring cell.
                    r, c = row + dr, col + dc

                    # Check:
                    # 1. Inside grid bounds
                    # 2. Is land ("1")
                    # 3. Not already visited
                    if (
                        r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit
                    ):

                        # Add neighbor to queue.
                        q.append((r, c))

                        # Mark as visited.
                        visit.add((r, c))

        # Traverse every cell in the grid.
        for r in range(rows):
            for c in range(cols):

                # Found unvisited land.
                if (
                    grid[r][c] == "1" and
                    (r, c) not in visit
                ):

                    # Explore the entire island.
                    bfs(r, c)

                    # Count this island.
                    islands += 1

        # Return total islands found.
        return islands