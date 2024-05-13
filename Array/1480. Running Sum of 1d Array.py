""" 
Link: https://leetcode.com/problems/running-sum-of-1d-array/description/
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        ans = []
        for num in nums:
          s += num
          ans.append(s)
        
        return ans