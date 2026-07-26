class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        j = 0
        for i in range(len(t)):
            if j == len(s) - 1:
                return True
            if s[j] == t[i]:
                j += 1
        return False
