class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Convert string to lowercase
        s = s.lower()

        # Store only alphanumeric characters
        filtered = ""

        # Keep only letters and numbers
        for c in s:

            # isalnum() returns True for:
            # a-z
            # A-Z
            # 0-9
            if c.isalnum():
                filtered += c

        # Reverse filtered string
        rev = filtered[::-1]

        # Compare original and reversed
        return filtered == rev