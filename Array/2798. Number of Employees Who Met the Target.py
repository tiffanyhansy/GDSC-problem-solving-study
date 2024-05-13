""" 
Link : https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
"""

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for emp in range(hours):
            if emp >= target:
                count+=1
        
        return count
            