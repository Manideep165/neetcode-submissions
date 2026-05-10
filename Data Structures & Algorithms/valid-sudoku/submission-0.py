class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Dictionary:
        # key   -> column number
        # value -> set of numbers already seen in that column
        #
        # Example:
        # cols[0] = {"5", "3"}
        cols = collections.defaultdict(set)

        # Dictionary:
        # key   -> row number
        # value -> set of numbers already seen in that row
        #
        # Example:
        # rows[1] = {"7", "9"}
        rows = collections.defaultdict(set)

        # Dictionary for 3x3 sub-boxes
        #
        # key = (r//3, c//3)
        #
        # This identifies which 3x3 square
        # the cell belongs to.
        #
        # Example:
        # (0,0) -> top-left square
        # (0,1) -> top-middle square
        # (1,2) -> middle-right square
        squares = collections.defaultdict(set)

        # Loop through all rows
        for r in range(9):

            # Loop through all columns
            for c in range(9):

                # Ignore empty cells
                if board[r][c] == ".":
                    continue

                # Current number in cell
                #
                # Example:
                # "5"
                val = board[r][c]

                # Check if number already exists:
                #
                # 1. in current row
                # 2. in current column
                # 3. in current 3x3 square
                #
                # If yes -> invalid Sudoku
                if (
                    val in rows[r] or
                    val in cols[c] or
                    val in squares[(r // 3, c // 3)]
                ):
                    return False

                # Add number into row set
                rows[r].add(val)

                # Add number into column set
                cols[c].add(val)

                # Add number into square set
                squares[(r // 3, c // 3)].add(val)

        # If no duplicates found,
        # Sudoku is valid
        return True