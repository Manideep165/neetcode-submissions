class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp[i] = number of 1-bits in binary representation of i
        dp = [0] * (n + 1)

        # Current power of 2
        offset = 1

        # Compute answers from 1 to n
        for i in range(1, n + 1):

            # If i reaches the next power of 2,
            # update the offset
            if offset * 2 == i:
                offset = i

            # Count bits using the previously computed value
            dp[i] = 1 + dp[i - offset]

        return dp