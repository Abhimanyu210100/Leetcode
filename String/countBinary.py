class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        count  = 0
        prev = 0
        curr = 1
        for i in range(1,len(s)):
            if s[i-1] != s[i]:
                count+=min(prev,curr)
                prev = curr
                curr=1    
            else:
                curr+=1
        #Counting for the last pair. After the string ends
        count+=min(prev,curr) 
        return count    
            
        
# def countBinarySubstrings(self, s: str) -> int:
# 	ans, prev, cur = 0, 0, 1
# 	for i in range(1, len(s)):
# 		if s[i] != s[i - 1]:
# 			ans += min(prev, cur)
# 			prev = cur
# 			cur = 1
# 		else:
# 			cur += 1
# 	ans += min(prev, cur)
# 	return ans