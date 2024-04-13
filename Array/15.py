# 3Sum
# 배열이 주어졌을 때 i!= j, i!= k, j!= k 같은 triplet [nums[i], nums[j], nums[k]] 반환 

class Solution:
    def threeSum(self, nums):
        results = []
        
        # 배열 정렬 
        nums.sort()

        # i가 최대일 때 left, right 존재하게 
        for i in range(len(nums) - 2):
          
            # 중복된 값은 skip 
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]
                
                if sum_val < 0:
                    left += 1
                    
                elif sum_val > 0:
                    right -= 1
                    
                else:
                    # sum = 0일 때 (정답, skip)
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return results
