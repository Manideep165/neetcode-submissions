class Solution:
    def hammingWeight(self, n: int) -> int:
        # Counts the number of 1 bits
        res = 0

        # Continue until all set bits are removed
        while n:

            # Remove the rightmost set bit (1)
            n &= (n - 1)

            # Count the removed bit
            res += 1

        # Return total number of 1 bits
        return res