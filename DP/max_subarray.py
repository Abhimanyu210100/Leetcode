class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max1 = nums[0]
        current = nums[0]
        for num in nums[1:]:
            current = max(num+current,num)
            max1 = max(current,max1)
        return max
