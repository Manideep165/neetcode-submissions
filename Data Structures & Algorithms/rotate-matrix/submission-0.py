class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Left and right boundaries of the current layer
        l, r = 0, len(matrix) - 1

        # Process layer by layer
        while l < r:

            # Number of elements in the current layer side - 1
            for i in range(r - l):

                top, bottom = l, r

                # Save top-left value
                topLeft = matrix[top][l + i]

                # Move bottom-left -> top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom-right -> bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top-right -> bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move saved top-left -> top-right
                matrix[top + i][r] = topLeft

            # Move to the next inner layer
            r -= 1
            l += 1