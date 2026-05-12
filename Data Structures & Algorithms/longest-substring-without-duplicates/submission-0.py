class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set stores current window characters
        #
        # Helps check duplicates in O(1)
        charSet = set()

        # Left pointer
        l = 0

        # Stores longest substring length
        res = 0

        # Right pointer expands window
        for r in range(len(s)):
            # If duplicate character found,
            # shrink window from left side
            #
            # Continue removing until
            # duplicate disappears
            while s[r] in charSet:
                # Remove left character
                charSet.remove(s[l])

                # Move left pointer right
                l += 1

            # Add current character
            charSet.add(s[r])

            # Current window length:
            #
            # right - left + 1
            #
            # Example:
            # l = 2
            # r = 4
            #
            # length = 3
            res = max(res, r - l + 1)
        # Return longest length
        return res
        