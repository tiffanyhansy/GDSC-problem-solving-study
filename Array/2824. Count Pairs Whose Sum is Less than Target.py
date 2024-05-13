""" 
Link : https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
"""

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
      
        ans = 0
        for i in range(len(nums)):
          for j in range(i+1, len(nums)):
            if 0 <= i < j < len(nums) and (nums[i] + nums[j] < target):
              ans+=1 
        return ans