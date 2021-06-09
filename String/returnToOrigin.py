class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = list(moves)
        if moves.count('U') != moves.count('D'): return 0
        if moves.count('L') != moves.count('R'): return 0
        return 1
        