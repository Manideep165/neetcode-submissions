class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in range(len(s)):
            if s[i] in stack:
                stack.pop()
            else:
                stack.append(s[i])

        if stack:
            return True
        else:
            return False
        