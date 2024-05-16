""" 
Link : https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/
"""

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        binary = bin(nums)
