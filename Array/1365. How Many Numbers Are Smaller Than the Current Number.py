""" 
Link : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for num1 in nums: 
          count = 0
          for num2 in nums:
            if num1 > num2: 
              count+=1 
        
          ans.append(count)
        
        return ans