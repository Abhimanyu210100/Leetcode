class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n==1:
            return 1
        if not trust and n!=1:
            return -1
        count = {}
        for i in range(len(trust)):
            if trust[i][1] not in count:
                count[trust[i][1]] = 1
            else:
                count[trust[i][1]] += 1
            if trust[i][0] not in count:
                count[trust[i][0]] = -1000
            else:
                count[trust[i][0]] -= 1000
        for i in count.keys():
            if count[i] == n-1:
                return i
        return -1