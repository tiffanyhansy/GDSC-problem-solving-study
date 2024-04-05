# Remove element 
# nums array에서 val 을 제외했을 때 남는 elements, 그 개수 k 

class Solution(object):
    def removeElement(self, nums, val):
      
      for i in range(len(nums)):
        if nums[0] != val: 
          nums.append(nums[0])  # 배열 뒤로 추가 
          del nums[0]
        
        else: del nums[0] # val과 같으니 배열애서 삭제
        
      return len(nums)  # 최종 배열 return
      
