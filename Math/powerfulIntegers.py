class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0: return []
        m = bound if x ==1 else int(log(bound,x))
        n = bound if y ==1 else int(log(bound,y))
        soln = list()
        for i in range(m+1):
            for j in range(n+1):
                value = x**i + y**j
                if value <= bound:
                    soln.append(value)
                if y == 1: break
            if x == 1:
                break
        return list(set(soln))
        