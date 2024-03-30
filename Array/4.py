# median 중앙값 구하기 
# merged array에서 요소의 개수가 홀수/짝수 나누어서 구하기 


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()

        n = len(nums)
        # merged array에서 요소 개수가 홀수 
        if n % 2 == 1:  
            ans = nums[n // 2]
            
        # merged array에서 요소 개수가 짝수
        else:  
            ans = (nums[n // 2 - 1] + nums[n // 2]) / 2.0

        return ans

        