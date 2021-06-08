class Solution:
    def rotatedDigits(self, n: int) -> int:
        dic = {
            '0' : '0',
            '1' : '1',
            '2' : '5',
            '5' : '2',
            '6' : '9',
            '8' : '8',
            '9' : '6'
        }
        count=0
        for i in range(2,n+1):
            s = str(i)
            temp_s = ''
            if '3' in s or '4' in s or '7' in s:
                continue
            else:
                for char in s:
                    temp_s += dic[char]
            if i != int(temp_s):
                count+=1
        return count
            
        