# 3Sum closest
# 길이 n, 정수 target이 있는 배열 nums 에서, 합이 target과 가장 가까운 3개의 nums 요소를 찾아 그 sum을 return 

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        # 배열 정렬 
        nums = sorted(nums)
        
        # result = 배열의 1번째, 2번째, 마지막 요소의 합
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        
        for i in range(len(nums) - 1 ): 
          left = i + 1 
          right = len(nums) - 1   # 마지막 pointer
          
          while left < right: 
            rn = nums[left] + nums[right] + nums[i]
            
            if rn == target: 
              return target
          
            elif abs(target - rn ) < abs(target - result): #abs : 절댓값 반환 함수 
              result = rn
              
            elif rn > target:
              right = right - 1 
            
            else:
              left = left + 1
            
        return result