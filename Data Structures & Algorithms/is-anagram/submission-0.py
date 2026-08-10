class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        result1, result2 = {}, {}
        for i in range(len(s)):
            result1[s[i]] = 1 + result1.get(s[i], 0)
            result2[t[i]] = 1 + result2.get(t[i], 0)

        for c in result1:
            if result1[c] != result2.get(c, 0):
                return False
        return True