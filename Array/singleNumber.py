class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums = sorted(nums)
        for i in range(0,len(nums)-1,2):
            print(i)
            if nums[i] == nums[i+1]:
                continue
            else:
                return nums[i]
        return nums[-1]
        