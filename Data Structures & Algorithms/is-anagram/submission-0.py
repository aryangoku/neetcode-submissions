from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t) or len(t) < len(s):
            return False
        a = Counter(s)
        b = Counter(t)
        for i in range(len(s)):
            if t[i] not in a or s[i] not in b:
                return False
            if a[t[i]] != b[t[i]]:
                return False
        return True 