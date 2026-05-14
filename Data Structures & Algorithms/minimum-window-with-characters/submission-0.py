class Solution:

    def minWindow(self, s: str, t: str) -> str:

        # If t is empty,
        # no window needed
        if t == "":
            return ""

        # Frequency map for t
        #
        # Example:
        # t = "AABC"
        #
        # countT =
        # {
        #   'A': 2,
        #   'B': 1,
        #   'C': 1
        # }
        countT = {}

        # Frequency map for current window
        window = {}

        # Build frequency map of t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have = number of characters
        # currently satisfying required frequency
        #
        # need = total unique characters needed
        have = 0
        need = len(countT)

        # Stores best window indices
        res = [-1, -1]

        # Length of smallest window found
        resLen = float("infinity")

        # Left pointer
        l = 0

        # Expand window using right pointer
        for r in range(len(s)):

            # Current character
            c = s[r]

            # Add character to window count
            window[c] = 1 + window.get(c, 0)

            # If current character frequency
            # matches target frequency,
            # increase have count
            if c in countT and window[c] == countT[c]:
                have += 1

            # While current window is valid
            #
            # meaning:
            # all required chars are present
            while have == need:

                # Update result if smaller window found
                if (r - l + 1) < resLen:

                    # Store indices
                    res = [l, r]

                    # Store length
                    resLen = (r - l + 1)

                # Remove left character
                window[s[l]] -= 1

                # If removing breaks requirement,
                # decrease have count
                if (
                    s[l] in countT and
                    window[s[l]] < countT[s[l]]
                ):
                    have -= 1

                # Shrink window
                l += 1

        # Extract final indices
        l, r = res

        # Return smallest substring
        #
        # If no valid window found,
        # return empty string
        return s[l:r + 1] if resLen != float("infinity") else ""        