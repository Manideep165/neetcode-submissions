class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a DP table with an extra row and column
        # dp[i][j] = LCS length of text1[i:] and text2[j:]
        dp = [
            [0 for j in range(len(text2) + 1)]
            for i in range(len(text1) + 1)
        ]

        # Fill the table from bottom-right to top-left
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):

                # If characters match,
                # include this character in the LCS
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                # Otherwise, skip one character
                # from either string and take the better result
                else:
                    dp[i][j] = max(
                        dp[i][j + 1],
                        dp[i + 1][j]
                    )

        # LCS length of the full strings
        return dp[0][0]