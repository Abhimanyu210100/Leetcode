class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        soln = [0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            one_step = soln[i-1]+cost[i-1]
            two_step = soln[i-2]+cost[i-2]
            soln[i] = min(one_step,two_step)
        return soln[-1]