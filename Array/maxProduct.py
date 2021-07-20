class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        for i in range(len(nums)):
            if nums[i] > max1:
                max1 = nums[i]
                ind = i
            
        for i in range(len(nums)):
            if nums[i] <= max1 and nums[i] > max2 and i != ind:
                max2 = nums[i]
                
        return (max1-1)*(max2-1)
        