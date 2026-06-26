class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # dp[i] = True if the substring s[i:] can be segmented
        # into words from the dictionary
        dp = [False] * (len(s) + 1)

        # Base case:
        # An empty string can always be segmented
        dp[len(s)] = True

        # Process the string from right to left
        for i in range(len(s) - 1, -1, -1):

            # Try every word in the dictionary
            for w in wordDict:

                # Check if the word fits within the remaining string
                # and matches the substring starting at index i
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:

                    # If the remaining substring after this word
                    # can also be segmented, mark dp[i] as True
                    dp[i] = dp[i + len(w)]

                # No need to check more words once dp[i] is True
                if dp[i]:
                    break

        # Return whether the entire string can be segmented
        return dp[0]