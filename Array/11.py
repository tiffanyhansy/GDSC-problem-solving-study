# i번째 선의 두 끝이 (i,0) (i, height[i])
# 두 선으로 이루어진 직사각형의 넓이가 가장 클 때의 직사각형의 넓이를 return 

class Solution(object):
    def maxArea(self, height):
        area = 0
        first  = 0  # (i,0)
        last = len(height) - 1  

        while last - first > 0:
            small = min(height[first], height[last])
            gap = (last - first) * small

            if height[last] > height[first]:
                first += 1
                
            else:
                last -= 1

            area = max(area, gap)

        return area

      
    
        """
        :type height: List[int]
        :rtype: int
        """
        