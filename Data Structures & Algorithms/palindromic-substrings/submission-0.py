class Solution:
    def countSubstrings(self, s: str) -> int:
        # Stores the total number of palindromic substrings
        res = 0

        # Treat each index as a possible center
        for i in range(len(s)):

            # ----- Odd-length palindromes -----
            # Example: "racecar" (center = 'e')
            l = r = i

            # Expand outward while characters match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Every successful expansion forms a palindrome
                res += 1

                # Expand further
                l -= 1
                r += 1

            # ----- Even-length palindromes -----
            # Example: "abba" (center = between the two 'b's)
            l = i
            r = i + 1

            # Expand outward while characters match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Every successful expansion forms a palindrome
                res += 1

                # Expand further
                l -= 1
                r += 1

        # Return total palindromic substrings found
        return res