class Solution:

    def characterReplacement(self, s: str, k: int) -> int:

        # Dictionary stores frequency
        # of characters inside current window
        #
        # Example:
        # {
        #   'A': 3,
        #   'B': 2
        # }
        count = {}

        # Stores longest valid substring length
        res = 0

        # Left pointer
        l = 0

        # Maximum frequency character
        # inside current window
        #
        # Example:
        # "AABAB"
        #
        # maxf = 3 because A appears 3 times
        maxf = 0

        # Right pointer expands window
        for r in range(len(s)):

            # Add current character frequency
            count[s[r]] = 1 + count.get(s[r], 0)

            # Update maximum frequency
            maxf = max(maxf, count[s[r]])

            # Current window size:
            #
            # r - l + 1
            #
            # Characters needing replacement:
            #
            # window_size - max_frequency
            #
            # If replacements needed exceed k,
            # shrink window
            while (r - l + 1) - maxf > k:

                # Remove left character
                count[s[l]] -= 1

                # Move left pointer right
                l += 1

            # Update longest valid window
            res = max(res, r - l + 1)

        # Return answer
        return res