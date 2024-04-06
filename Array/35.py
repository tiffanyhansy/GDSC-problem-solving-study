# Search insert position 
# target 이 있으면 index 반환, target 없으면 있어야 할 index 반환 

class Solution(object):
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1 
        
        while start <= end:
          m = ( start + ( end - start )) // 2
          
          if nums[m] == target: #binary search 성공
            return m
          
          elif nums[m] < target:  #binary search에서 target 보다 왼쪽
            start = m + 1
            
          else: end = m - 1 #binary search에서 target 보다 오른쪽
          
        return start 