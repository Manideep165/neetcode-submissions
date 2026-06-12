class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # Number of rows and columns.
        ROWS, COLS = len(heights), len(heights[0])

        # Cells that can reach the Pacific Ocean.
        pac = set()

        # Cells that can reach the Atlantic Ocean.
        atl = set()

        def dfs(r, c, visit, prevHeight):

            # Stop if:
            # 1. Out of bounds
            # 2. Already visited
            # 3. Current height is lower than previous height
            if (
                (r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight
            ):
                return

            # Mark current cell as reachable.
            visit.add((r, c))

            # Explore all four directions.
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Start DFS from Pacific borders (top and left edges).
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])

            # Start DFS from Atlantic border (bottom edge).
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # Start DFS from Pacific border (left edge)
        # and Atlantic border (right edge).
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # Cells reachable from both oceans.
        res = []

        for r in range(ROWS):
            for c in range(COLS):

                # If both oceans can reach this cell.
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res