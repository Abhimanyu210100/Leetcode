class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # temp = digits[-1]
        # if temp == 9:
        #     i = -1
        #     while temp == 9:
        #         digits[i] = 0
        #         i-=1
        #         try:
        #             temp = digits[i]
        #         except: 
        #             break
        #     if abs(i)-1 == len(digits):
        #         digits.insert(0,1)
        #     else:
        #         digits[len(digits)-abs(i)]+=1
        # else:
        #     digits[-1] += 1
        # return digits
        temp=''
        for i in digits:
            temp+=str(i)
        digits = str(int(temp)+1)
        return list(digits)
        