class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxTime = releaseTimes[0]
        soln = [keysPressed[0]]
        for i in range(1,len(releaseTimes)):
            if releaseTimes[i]-releaseTimes[i-1] > maxTime:
                soln = []
                maxTime = releaseTimes[i]-releaseTimes[i-1]
            if releaseTimes[i]-releaseTimes[i-1] == maxTime:
                soln.append(keysPressed[i])
        list_ord = [ord(x) for x in soln]
        return soln[list_ord.index(max(list_ord))]
                
        