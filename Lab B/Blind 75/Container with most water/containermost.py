class Solution:
    def maxArea(self, height: List[int]) -> int:
        startLen = 0
        endLen = len(height) - 1
        maxArea = 0
        while startLen < endLen:
            currentArea = min(height[startLen],height[endLen]) * (endLen - startLen)
            maxArea = max(maxArea, currentArea)

            if(height[startLen] < height[endLen]):
                startLen = startLen + 1
            else:
                endLen = endLen - 1
        return maxArea