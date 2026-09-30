class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Forgot to check length parity first!
        if len(s) != len(t):
            return False
        
        d = {}
        for e in s:
            d[e] = d.get(e, 0) + 1

        for e in t:

            if e not in d or d[e] == 0:
                return False
            else:
                d[e] = d.get(e) - 1

        return True 

        