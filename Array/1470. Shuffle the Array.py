"""
Link : https://leetcode.com/problems/shuffle-the-array/
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
      ans = []
      for i in range(2*n):
        if i % 2 == 0:
          ans.append(nums[i // 2])
        
        else: 
          ans.append(nums[n+i // 2])
        
      return ans
      
  