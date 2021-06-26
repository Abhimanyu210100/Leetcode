class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # len1 = len(nums1)
        # len2 = len(nums2)
        # soln = []
        # if len1>len2:
        #     for i in range(len1):
        #         if nums1[i] in nums2:
        #             soln.append(nums1[i])
        #             nums2.remove(nums1[i])
        # else:
        #     for i in range(len2):
        #         if nums2[i] in nums1:
        #             soln.append(nums2[i])
        #             nums1.remove(nums2[i])
        # return soln
    
        count = {}
        soln =[]
        for i in nums1:
            if i not in count:
                count[i] = 1
            else:
                count[i]+=1
        for i in nums2:
            if i in count and count[i] != 0:
                count[i] -= 1
                soln.append(i)
        return soln
                
        
        