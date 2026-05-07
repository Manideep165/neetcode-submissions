class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dup = set()
        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
        