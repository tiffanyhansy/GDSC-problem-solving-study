# Plus One 
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits):
       
        # 배열 끝에서 시작 
        for i in range(len(digits) - 1, -1, -1):
            
            if digits[i] < 9:
                digits[i] += 1
                return digits
              
            else: 
              digits[i] = 0
              
        # 모든 digits가 9라면 시작에 new digit 1 추가 
        return [1] + digits
