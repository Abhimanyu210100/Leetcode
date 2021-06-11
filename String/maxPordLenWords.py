class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_val = 0
        dic = {}
        for word in words:
            dic[word] = set(word)
        
        for i in range(len(words)-1):
            set1 = dic[words[i]]
            for j in range(i+1,len(words)):
                set2 = dic[words[j]]
                truth_val = True
                if len(set1)>len(set2):
                    for c in set2:
                        if c in set1:
                            truth_val = False
                            break
                else:
                    for c in set1:
                        if c in set2:
                            truth_val = False
                            break
                if truth_val:
                    max_val = max(max_val, len(words[i])*len(words[j]))
        return max_val
        
        
        
#         max_val = 0
#         for i in range(len(words)):
#             for j in range(i+1,len(words)):
#                 list1 = list(words[i])
#                 list2 = list(words[j])
#                 if len(list1)*len(list2) <= max_val: 
#                     continue
#                 if not set(list1).intersection(set(list2)):
#                     if len(list1)*len(list2) > max_val: 
#                         max_val = len(list1)*len(list2)
        
#         return max_val
        