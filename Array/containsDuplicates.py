class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums = sorted(nums)
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return 1
        # return 0
        
        dic = set()
        for i in range(len(nums)):
            if nums[i] in dic:
                return 1
            else:
                dic.add(nums[i])
        return 0