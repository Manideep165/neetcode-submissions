class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Get the number of rows and columns in the board.
        ROWS, COLS = len(board), len(board[0])

        # Stores cells currently being used in the search path.
        # Prevents revisiting the same cell in a single word path.
        path = set()

        def dfs(r, c, i):

            # If we've matched all characters in the word,
            # the word exists in the board.
            if i == len(word):
                return True

            # Invalid cases:
            # 1. Out of bounds
            # 2. Character doesn't match
            # 3. Cell already used in current path
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path
            ):
                return False

            # Mark current cell as visited.
            path.add((r, c))

            # Explore all 4 directions.
            res = (
                dfs(r + 1, c, i + 1) or  # Down
                dfs(r - 1, c, i + 1) or  # Up
                dfs(r, c + 1, i + 1) or  # Right
                dfs(r, c - 1, i + 1)     # Left
            )

            # Backtrack: remove current cell before returning.
            path.remove((r, c))

            return res

        # Try starting the word from every cell.
        for r in range(ROWS):
            for c in range(COLS):

                # If a valid path is found, return True.
                if dfs(r, c, 0):
                    return True

        # Word was not found anywhere in the board.
        return False