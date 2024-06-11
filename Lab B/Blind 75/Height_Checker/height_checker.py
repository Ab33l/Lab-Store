'''
If current heights list is to be sorted, how many elements are in their current wrong indices
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.
'''
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expectedHeight = sorted(heights)
        variations = 0
        for h in range(len(expectedHeight)):
            if expectedHeight[h] != heights[h]:
                variations += 1
        return variations
