class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd_ind = []
        even_ind = []
        for i in range(len(nums)):
            if nums[i]%2 == 0 and i%2 == 0:
                continue
            if nums[i]%2 == 1 and i%2 == 1:
                continue
            if nums[i]%2 == 0 and i%2 == 1:
                odd_ind.append(i)
            if nums[i]%2 == 1 and i%2 == 0:
                even_ind.append(i)
        if odd_ind == []:
            return nums
        for i in range(len(odd_ind)):
            temp = nums[odd_ind[i]]
            nums[odd_ind[i]] = nums[odd_ind[i]] + nums[even_ind[i]]
            nums[even_ind[i]] = nums[odd_ind[i]] - nums[even_ind[i]]
            nums[odd_ind[i]] = nums[odd_ind[i]] - nums[even_ind[i]]
        return nums