class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Stores the longest palindrome found so far
        res = ""

        # Length of the longest palindrome
        resLen = 0

        # Try expanding around every character
        for i in range(len(s)):

            # ----- Odd-length palindrome -----
            # Example: "racecar" (center = e)
            l, r = i, i

            # Expand outward while characters match
            while l >= 0 and r < len(s) and s[l] == s[r]:

                # Check if current palindrome is longer
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1

                # Expand outward
                l -= 1
                r += 1

            # ----- Even-length palindrome -----
            # Example: "abba" (center = bb)
            l, r = i, i + 1

            # Expand outward while characters match
            while l >= 0 and r < len(s) and s[l] == s[r]:

                # Check if current palindrome is longer
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1

                # Expand outward
                l -= 1
                r += 1

        # Return the longest palindrome found
        return res