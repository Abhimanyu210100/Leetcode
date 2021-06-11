class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        soln = []
        for i in range(n):
            soln.append(nums[i])
            soln.append(nums[n+i])
        return soln
        