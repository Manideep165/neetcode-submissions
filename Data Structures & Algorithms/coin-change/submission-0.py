class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = minimum number of coins needed to make amount i
        # Initialize with an impossible large value (amount + 1)
        dp = [amount + 1] * (amount + 1)

        # Base case:
        # 0 coins are needed to make amount 0
        dp[0] = 0

        # Calculate answers for amounts from 1 to target amount
        for a in range(1, amount + 1):

            # Try every coin denomination
            for c in coins:

                # If coin can contribute to current amount
                if a - c >= 0:

                    # Either keep current answer
                    # or use coin c and add 1 coin
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # If dp[amount] was never updated,
        # the amount cannot be formed
        return dp[amount] if dp[amount] != amount + 1 else -1