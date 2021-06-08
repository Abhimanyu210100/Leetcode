class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        if len(s)%2 == 0: n = int(len(s)/2)
        else: n = int((len(s)-1)/2)
        for i in range(n):
            if s[i] == s[len(s)-1-i]: continue
            else: return 0
        return 1
        