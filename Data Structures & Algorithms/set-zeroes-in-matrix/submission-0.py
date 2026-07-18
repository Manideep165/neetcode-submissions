class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Tracks whether the first row originally contains a zero
        rowZero = False

        # Use the first row and first column as markers
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:

                    # Mark the entire column
                    matrix[0][c] = 0

                    # Mark the entire row
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # Zero out cells based on the row/column markers
        for r in range(1, ROWS):
            for c in range(1, COLS):

                # If either the row or column is marked,
                # set the current cell to zero
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # If the first column is marked,
        # zero out the entire first column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # If the first row originally had a zero,
        # zero out the entire first row
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0