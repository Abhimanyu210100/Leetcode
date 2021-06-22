class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        count = 0
        s = list(s)
        length = len(s)
        for i in range(len(t)):
            if s == None: return True
            if t[i] == s[0]:
                s.pop(0)
                count+=1
                if count == length: return True
        return False
                
        