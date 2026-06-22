class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = number of ways to decode substring s[i:]
        dp = {len(s): 1}

        # Process the string from right to left
        for i in range(len(s) - 1, -1, -1):

            # A substring starting with '0' cannot be decoded
            if s[i] == "0":
                dp[i] = 0
            else:
                # Take the single-digit decoding
                dp[i] = dp[i + 1]

            # Check if a valid two-digit decoding exists
            if (
                i + 1 < len(s)
                and (
                    s[i] == "1"
                    or (s[i] == "2" and s[i + 1] in "0123456")
                )
            ):
                dp[i] += dp[i + 2]

        # Number of ways to decode the entire string
        return dp[0]