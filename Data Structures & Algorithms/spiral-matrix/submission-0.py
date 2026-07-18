class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Stores the elements in spiral order
        res = []

        # Initialize the four boundaries
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # Continue while there is at least one row and one column left
        while left < right and top < bottom:

            # Traverse the top row (left → right)
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Traverse the right column (top → bottom)
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # If no rows or columns remain, stop
            if not (left < right and top < bottom):
                break

            # Traverse the bottom row (right → left)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Traverse the left column (bottom → top)
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        # Return the spiral traversal
        return res