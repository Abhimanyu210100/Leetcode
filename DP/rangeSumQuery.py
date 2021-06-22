class NumArray:

    def __init__(self, nums: List[int]):
        self.NumArray = nums
        self.sum_mat = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.sum_mat[i+1] = nums[i] + self.sum_mat[i]
            
        
    def sumRange(self, left: int, right: int) -> int:
        #Approach 1
        # sum1 = 0
        # for i in range(left,right+1):
        #     sum1+=self.NumArray[i]
        # return sum1
        #Approach 2
        return self.sum_mat[right+1] - self.sum_mat[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)