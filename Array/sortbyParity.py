class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_nums = []
        odd_nums = []
        for num in nums:
            if num%2==0: even_nums.append(num)
            if num%2==1: odd_nums.append(num)
        return even_nums+odd_nums
        