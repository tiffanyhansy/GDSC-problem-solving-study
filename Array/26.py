class Solution(object):
    def removeDuplicates(self, nums):
      
      if len(nums) < 2:
            return len(nums)
      a = 0
      
      for cur in range(1,len(nums)):
        if nums[cur] != nums[a]:
          a += 1
          nums[a] = nums[cur]

        return a + 1