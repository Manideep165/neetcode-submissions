class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Represents the bottom row of the grid.
        # Every cell in the last row has exactly 1 path to the destination
        row = [1] * n

        # Build rows from bottom to top
        for i in range(m - 1):

            # The rightmost column always has 1 path
            newRow = [1] * n

            # Fill the current row from right to left
            for j in range(n - 2, -1, -1):

                # Paths = paths from the cell to the right
                #       + paths from the cell below
                newRow[j] = newRow[j + 1] + row[j]

            # Move up one row
            row = newRow

        # Top-left cell contains the final answer
        return row[0]